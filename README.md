# 🏥 HDIMS - Health Data Information & Management System

HDIMS is a web-based and mobile-compatible application built using **Flask** for real-time, role-based health data management in hospitals and government departments.

It helps streamline data flow across Reception, Lab, Pharmacy, and Admin departments while providing a live monitoring dashboard to the Super Admin. The system also supports Google OAuth login and user role segregation.

---

## 🚀 Features

- 🔐 User Authentication (Email/Password + Google Login)
- 🧑‍⚕️ Role-based Dashboards:
  - **Reception** – Patient registration and data entry
  - **Pharmacy** – Medicine inventory and sales tracking
  - **Lab** – Lab stock upload and test management
  - **Admin** – View hospital budget, logs, and notifications
- 📊 Super Admin Dashboard – Monitor data from all departments
- 🗃️ Database: SQLite with SQLAlchemy ORM
- 💻 Frontend: HTML5 + CSS3 (Gradient UI, Responsive)
- ☁️ Google OAuth 2.0 Integrated Login

---

## 🔧 Technologies Used

| Frontend | Backend | Database | Auth |
|---------|----------|----------|------|
| HTML, CSS (No JS frameworks) | Python Flask | SQLite (SQLAlchemy) | Flask-Login, Flask-Dance (Google OAuth) |

---

## 🛠️ Setup Instructions

### 1. 📁 Clone this repository
```bash
git clone https://github.com/your-username/hdims-app.git
cd hdims-app
