from flask import Flask, request

app = Flask(__name__)

students = [
    ("Rahul", 20, "BCA", 85),
    ("Anjali", 21, "BTech", 90),
    ("Kiran", 19, "BSc", 78),
    ("Sneha", 22, "BBA", 88),
    ("Arjun", 20, "BCom", 82)
]

@app.route("/", methods=["GET", "POST"])
def home():

    global students

    if request.method == "POST":

        name = request.form["name"]
        age = request.form["age"]
        course = request.form["course"]
        marks = request.form["marks"]

        students.append((name, age, course, marks))

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

    form {
        margin-bottom: 20px;
        background: white;
        padding: 20px;
        width: 50%;
    }

    input {
        padding: 10px;
        margin: 5px;
        width: 90%;
    }

    button {
        padding: 10px 20px;
        background-color: green;
        color: white;
        border: none;
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

    <form method="POST">

        <input type="text" name="name" placeholder="Student Name" required><br>

        <input type="number" name="age" placeholder="Age" required><br>

        <input type="text" name="course" placeholder="Course" required><br>

        <input type="number" name="marks" placeholder="Marks" required><br>

        <button type="submit">Add Student</button>

    </form>

    <table>

        <tr>
            <th>ID</th>
            <th>Name</th>
            <th>Age</th>
            <th>Course</th>
            <th>Marks</th>
        </tr>
    """

    for i, row in enumerate(students, start=1):

        html += f"""
        <tr>
            <td>{i}</td>
            <td>{row[0]}</td>
            <td>{row[1]}</td>
            <td>{row[2]}</td>
            <td>{row[3]}</td>
        </tr>
        """

    html += """
    </table>

    </body>
    </html>
    """

    return html


if __name__ == "__main__":
    app.run()
