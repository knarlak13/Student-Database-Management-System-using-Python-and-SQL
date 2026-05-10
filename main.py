from flask import Flask
import sqlite3

app = Flask(__name__)

@app.route("/")
def home():

    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            age INTEGER,
            course TEXT,
            marks INTEGER
        )
    """)

    students = [
        ("Rahul", 20, "BCA", 85),
        ("Anjali", 21, "BTech", 90),
        ("Kiran", 19, "BSc", 78),
        ("Sneha", 22, "BBA", 88),
        ("Arjun", 20, "BCom", 82)
    ]

    cursor.executemany("""
        INSERT INTO students (name, age, course, marks)
        VALUES (?, ?, ?, ?)
    """, students)

    conn.commit()

    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()

    html = "<h1>Student Database</h1>"

    for row in rows:
        html += f"<p>{row}</p>"

    conn.close()

    return html


if __name__ == "__main__":
    app.run()
