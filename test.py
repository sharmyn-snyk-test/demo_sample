from flask import Flask, request, render_template_string, send_file
import sqlite3
import os

app = Flask(__name__)

# ❌ Hardcoded secret key (BAD PRACTICE)
SECRET_KEY = "hardcoded-secret"

# ❌ Insecure database connection (No parameterized queries)
def get_db_connection():
    conn = sqlite3.connect("users.db")
    conn.row_factory = sqlite3.Row
    return conn

# ❌ SQL Injection Vulnerability
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        conn = get_db_connection()
        query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
        user = conn.execute(query).fetchone()
        conn.close()

        if user:
            return f"Welcome, {username}!"
        else:
            return "Invalid credentials!"

    return '''
        <form method="post">
            Username: <input type="text" name="username"><br>
            Password: <input type="password" name="password"><br>
            <input type="submit" value="Login">
        </form>
    '''

# ❌ Cross-Site Scripting (XSS) Vulnerability
@app.route("/greet")
def greet():
    name = request.args.get("name", "Guest")
    return render_template_string(f"<h1>Hello, {name}!</h1>")  # No sanitization

# ❌ Insecure File Upload
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/upload", methods=["POST"])
def upload_file():
    file = request.files["file"]
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)  # No validation of file type
    file.save(file_path)
    return f"File uploaded: {file.filename}"

# ❌ Insecure File Download (Path Traversal)
@app.route("/download/<filename>")
def download(filename):
    return send_file(os.path.join(UPLOAD_FOLDER, filename))  # No path validation

if __name__ == "__main__":
    app.run(debug=True)
