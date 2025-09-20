import os
from flask import Flask, redirect, url_for
from dotenv import load_dotenv
from flask_dance.contrib.google import make_google_blueprint, google
from extensions import db, login_manager
from flask_login import login_user

# Load env
load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", "supersecretkey")

# DB setup
db_folder = os.path.join(os.path.abspath(os.path.dirname(__file__)), "database")
os.makedirs(db_folder, exist_ok=True)
db_path = os.path.join(db_folder, "hdims.db")
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{db_path.replace(os.sep, '/')}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
login_manager.init_app(app)
login_manager.login_view = 'auth.login'

# Import models
from models.user import User

# ---------------------------
# Google OAuth Blueprint
# ---------------------------
google_bp = make_google_blueprint(
    client_id=os.getenv("GOOGLE_CLIENT_ID"),
    client_secret=os.getenv("GOOGLE_CLIENT_SECRET"),
    scope=["profile", "email"],
    redirect_url="http://127.0.0.1:5000/login/google/authorized"
)
app.register_blueprint(google_bp, url_prefix="/login")

# Google login callback
@app.route("/login/google/authorized")
def google_login_callback():
    if not google.authorized:
        return redirect(url_for("google.login"))

    resp = google.get("/oauth2/v2/userinfo")
    if resp.ok:
        info = resp.json()
        email = info["email"]
        username = info.get("name", email.split("@")[0])

        user = User.query.filter_by(email=email).first()
        if not user:
            user = User(username=username, email=email, password="oauth", role="reception")
            db.session.add(user)
            db.session.commit()

        login_user(user)
        return redirect(url_for("dashboard.dashboard_home"))

    return "⚠️ Google login failed", 400

# User loader
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Blueprints
from routes.auth_routes import auth_bp
from routes.dashboard_routes import dashboard_bp
# ... other blueprints
app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(dashboard_bp, url_prefix='/dashboard')

# Default route
@app.route('/')
def home():
    return redirect(url_for('auth.login'))

# Run app
if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
