Student Database Management System using Python & SQL
📌 Project Overview

The Student Database Management System is a beginner-friendly database project developed using Python and SQL.
This project demonstrates how to create and manage a database, import records from a CSV file, and perform basic database operations using SQL queries in Python.

The system reads student data from a CSV file and stores it in an SQL database table. It then retrieves and displays all stored records successfully.

🚀 Features
Create SQL database automatically
Create student table using SQL schema
Import student records from CSV file
Insert records into database
Fetch and display stored data
Beginner-friendly mini DBMS project
🛠 Technologies Used
Python
SQL
CSV File Handling
📂 Project Structure
database-project/
│
├── main.py            # Main Python program
├── schema.sql         # SQL table creation script
├── data.csv           # Student dataset
├── database.db        # SQLite database file
├── requirements.txt   # Project requirements
└── README.md          # Project documentation
⚙️ How It Works
Connects to the SQL database
Creates the students table using schema.sql
Reads student records from data.csv
Inserts records into the database
Retrieves and displays all stored records
📊 Sample Output
(1, 'Rahul', 20, 'BCA', 85)
(2, 'Anjali', 21, 'BTech', 90)
(3, 'Kiran', 19, 'BSc', 78)
(4, 'Sneha', 22, 'BBA', 88)
(5, 'Arjun', 20, 'BCom', 82)
🧠 Concepts Covered
Database connectivity using Python
SQLite database operations
SQL table creation
CSV file handling
Data insertion using SQL queries
Fetching and displaying records
▶️ Installation & Execution
Step 1: Clone Repository
git clone https://github.com/your-username/student-database-management-system.git
Step 2: Navigate to Project Folder
cd student-database-management-system
Step 3: Run the Project
python main.py
🗃 Database Schema
CREATE TABLE students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER,
    course TEXT,
    marks INTEGER
);
📁 Sample CSV Data
name,age,course,marks
Rahul,20,BCA,85
Anjali,21,BTech,90
Kiran,19,BSc,78
Sneha,22,BBA,88
Arjun,20,BCom,82
🎯 Learning Outcomes

By completing this project, you can understand:

How databases work in Python
Basics of SQL 
Importing structured data from CSV files
Performing CRUD-related database operations
🔮 Future Improvements
Add Update and Delete operations
Create GUI using Tkinter
Add search functionality
Build a web version using Flask or Django
