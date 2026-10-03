# Login Security Monitoring System

## 📌 Project Overview

The Login Security Monitoring System is a Flask-based web application designed to monitor and record user login activities.

The system detects successful and failed login attempts and generates a security alert when multiple failed login attempts are detected.

## 🎯 Objectives

- Monitor login activities
- Detect failed login attempts
- Track suspicious login behavior
- Store login records securely using SQLite
- Generate security alerts for repeated failed attempts

## 🚀 Features

- User login interface
- Successful login detection
- Failed login detection
- Failed attempt counter
- Suspicious login alert
- IP address logging
- Login time tracking
- SQLite database storage
- Web-based interface using Flask

## 🛠️ Technologies Used

- Python
- Flask
- SQLite
- HTML
- CSS
- Git & GitHub

## 📂 Project Structure

```text
login-security-monitor/
│
├── app.py
├── database.py
├── login_monitor.db
├── templates/
│   └── login.html
├── static/
├── .gitignore
└── README.md
⚙️ Installation

Clone the repository:

git clone https://github.com/nakshatraragupathir-beep/login-security-monitor.git

Move into the project directory:

cd login-security-monitor

Create a virtual environment:

python3 -m venv venv

Activate the virtual environment:

source venv/bin/activate

Install Flask:

pip install flask

Create the database:

python3 database.py
▶️ Running the Application

Start the Flask application:

python3 app.py

Open the browser and visit:

http://127.0.0.1:5000
🔐 Demo Credentials
Username: admin
Password: admin123
🚨 Security Monitoring

If an incorrect password is entered repeatedly, the system counts the failed attempts.

After three consecutive failed login attempts, the application displays:

SECURITY ALERT: Suspicious login detected!

The following information is stored in the database:

Username
IP Address
Login Status
Login Time
Number of Failed Attempts
🗄️ Database

The project uses SQLite to store login activity.

Database file:

login_monitor.db

The database contains a login_logs table for storing login events.

🔮 Future Enhancements
AI-based suspicious login detection
Email security alerts
Admin dashboard
Login activity charts
Geographic IP analysis
Machine learning-based anomaly detection
👩‍💻 Author

R. Nakshatra Manjari

B.Sc. Digital Forensics and Cyber Security

School of Quantum & Computing AI

📄 License

This project is developed for educational and academic purposes.


### Save panna

Nano-la:

**Ctrl + O** → Enter

Then:

**Ctrl + X**

### GitHub-ku update push panna

```bash
git add README.md

then:

git commit -m "Add professional README"

then:

git push

Ippo first git add README.md mattum run pannu.

