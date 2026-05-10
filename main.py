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

    html = """
    <html>
    <head>
        <title>Student Database</title>

        <style>
            body {
                font-family: Arial;
                padding: 40px;
                background-color: #f4f4f4;
            }

            h1 {
                color: #333;
            }

            table {
                border-collapse: collapse;
                width: 80%;
                background: white;
            }

            th, td {
                border: 1px solid #ddd;
                padding: 12px;
                text-align: center;
            }

            th {
                background-color: #4CAF50;
                color: white;
            }

            tr:nth-child(even) {
                background-color: #f2f2f2;
            }
        </style>
    </head>

    <body>

        <h1>Student Database Management System</h1>

        <table>
            <tr>
                <th>ID</th>
                <th>Name</th>
                <th>Age</th>
                <th>Course</th>
                <th>Marks</th>
            </tr>
    """

    for row in rows:
        html += f"""
            <tr>
                <td>{row[0]}</td>
                <td>{row[1]}</td>
                <td>{row[2]}</td>
                <td>{row[3]}</td>
                <td>{row[4]}</td>
            </tr>
        """

    html += """
        </table>

    </body>
    </html>
    """

    conn.close()

    return html
