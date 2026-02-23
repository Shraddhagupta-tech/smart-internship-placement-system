# Database Setup Guide
Smart Internship and Placement Management System

This guide explains how to set up the MySQL database required to run the project.

---

## 1. Install MySQL
Download and install MySQL Server if not already installed.

Verify installation:
mysql --version

---

## 2. Create Database
Login to MySQL:

mysql -u root -p

Create database:

CREATE DATABASE internship_management;

Use database:

USE internship_management;

---

## 3. Import Database Schema and Data
The project includes an exported SQL file containing tables and sample data.

Run:

SOURCE database/exported_database.sql;

(Replace file name if different)

This will create all required tables:
- user
- student
- internship
- application
- skill
- student_skill
- internship_skill

---

## 4. Configure Environment Variables
Create a `.env` file in the project root.

Add your database credentials:

DB_HOST=localhost
DB_USER=root
DB_PASSWORD=your_mysql_password
DB_NAME=internship_management

⚠ Do NOT commit this file to GitHub.

---

## 5. Install Python Dependencies

pip install -r requirements.txt

---

## 6. Run the Application

python app.py

Open browser:
http://127.0.0.1:5000

---

## 7. Default Behavior
- Application status default = "Applied"
- Application date default = current date
- Duplicate applications are restricted
- Passwords stored using hashing

---

## 8. Troubleshooting

Connection error  
✔ Check MySQL is running  
✔ Verify credentials in `.env`

Tables not found  
✔ Ensure SQL file imported correctly

Login not working  
✔ Check user table contains registered users

---

Database setup complete.