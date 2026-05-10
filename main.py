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

    # Insert data from CSV
    with open("data.csv", "r") as file:
        reader = csv.DictReader(file, skipinitialspace=True)

        for row in reader:
            cursor.execute("""
                INSERT OR IGNORE INTO students (name, age, course, marks)
                VALUES (?, ?, ?, ?)
            """, (
                row['name'],
                row['age'],
                row['course'],
                row['marks']
            ))

    conn.commit()

    # Fetch data
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()

    conn.close()

    html = "<h1>Student Database</h1>"

    for row in rows:
        html += f"<p>{row}</p>"

    return html


if __name__ == "__main__":
    app.run()
