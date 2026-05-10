 
import sqlite3
import csv

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
            INSERT INTO students (name, age, course, marks)
            VALUES (?, ?, ?, ?)
        """, (row['name'], row['age'], row['course'], row['marks']))

conn.commit()

# Display data
cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()
