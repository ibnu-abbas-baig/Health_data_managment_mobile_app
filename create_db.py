# create_db.py
from app import app, db

# Import models only, do not import routes/forms
from models.user import User
from models.patient import Patient
from models.medicine import Medicine
from models.sale import Sale
from models.lab_test import LabTest
from models.hospital_budget import HospitalBudget

# Create database and tables
with app.app_context():
    db.create_all()
    print("✅ Database created successfully as 'hdims.db'")
