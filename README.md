🎓 Internship & Placement Management System
A full-stack web application that manages student internship applications, tracks placement performance, and provides analytics for decision-making.
This system simulates a real-world campus placement environment where students apply for internships, organizations post opportunities, and administrators analyze outcomes using data-driven insights.

🚀 Project Overview
The Internship & Placement Management System is designed to:
Manage student and internship data
Allow students to apply for internships
Prevent duplicate applications
Automatically validate application records
Track placement and selection statistics
Provide analytics dashboards for performance monitoring

The application integrates a relational database with a web interface to demonstrate real-world backend and data management concepts.

✨ Key Features

👨‍🎓 Student Management
View all student records
Track academic details (CGPA, attendance, backlogs)
Store and manage student skills

🏢 Internship Management
Maintain internship listings with eligibility criteria
Track stipend, duration, and company details
Associate required skills with internships

📄 Application System
Students can apply for internships
Automatic application ID generation
Duplicate application prevention
Default application status and date
Real-time database upates

📊 Analytics Dashboard
Provides meaningful insights such as:
Total students, internships, and applications
Placement rate
Internship performance statistics
Branch-wise selection analysis
Most demanded skills
Skills of selected students

🔐 Authentication System
User registration and login
Password hashing for security
Session-based route protection

🛠 Tech Stack

Frontend:
HTML
Bootstrap (UI styling)

Backend:
Python
Flask (web framework)

Database:
MySQL (relational database)

Security:
Password hashing
Session management

🗄 Database Design

Main entities in the system:
Student
Company
Internship
Skill
Application
Student_Skill
Internship_Skill
User (authentication)

The database enforces:
Primary keys
Foreign key relationships
Cascading rules
Unique constraints
Data validation rules

📈 Analytics Implemented
The system performs SQL-based analytical queries including:
Placement rate calculation
Internship applicant distribution
Branch-wise selection performance
Skill demand trends
Skill success correlation
These analytics help simulate real organizational reporting.

🧠 Learning Outcomes
This project demonstrates practical understanding of:
Relational database design and normalization
SQL joins, aggregation, and analytics queries
Backend web development with Flask
Authentication and session handling
Data integrity enforcement
Full-stack integration
Real-world system modeling

📂 Project Structure
project/
│
├── app.py
├── database.py
│
├── templates/
│   ├── index.html
│   ├── login.html
│   ├── register.html
│   ├── students.html
│   ├── internships.html
│   ├── apply.html
│   └── analytics.html
│
└── database/
    └── db_schema.sql
    
⚙️ How to Run the Project
Clone the repository
Install dependencies
pip install flask mysql-connector-python werkzeug
Configure database connection in database.py
Run the application
python app.py
Open browser:
http://127.0.0.1:5000

🔮 Future Improvements
Planned enhancements:
Navigation bar UI improvements
Better alert and notification styling
Dropdown-based internship application form
Role-based access control (admin/student)
Charts and visual analytics
Email notifications
Resume upload support

🎯 Use Case
This project can be used as:
Academic DBMS / Web Development project
Placement cell management prototype
Backend portfolio project
Analytics-driven application tracking system

👩‍💻 Author
Shraddha Gupta
