from flask import Flask
import sqlite3
import csv

app = Flask(__name__)

@app.route("/")
def home():

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    # Create table
    with open("schema.sql", "r") as f:
        cursor.executescript(f.read())

    # Insert data
    with open("data.csv", "r") as file:
        reader = csv.DictReader(file, skipinitialspace=True)

        for row in reader:
            cursor.execute("""
                INSERT INTO students (name, age, course, marks)
                VALUES (?, ?, ?, ?)
            """, (row['name'], row['age'], row['course'], row['marks']))

    conn.commit()

    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()

    conn.close()

    return str(rows)
