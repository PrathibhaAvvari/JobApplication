"""
Job Application Tracker - Backend (Flask + SQLite)

This is a simple beginner-friendly fullstack app.
It has 4 basic API routes to Create, Read, Update, and Delete job applications.
"""

from flask import Flask, request, jsonify, render_template
import sqlite3

app = Flask(__name__)
DB_NAME = "jobs.db"


# ---------------------------
# Database setup
# ---------------------------
def init_db():
    """Create the jobs table if it doesn't already exist."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS jobs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            company TEXT NOT NULL,
            role TEXT NOT NULL,
            date_applied TEXT,
            status TEXT DEFAULT 'Applied',
            notes TEXT
        )
    """)
    conn.commit()
    conn.close()


def get_db_connection():
    """Helper: open a connection where rows behave like dictionaries."""
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn


# ---------------------------
# Frontend route
# ---------------------------
@app.route("/")
def home():
    return render_template("index.html")


# ---------------------------
# API routes
# ---------------------------

# READ: get all job applications
@app.route("/api/jobs", methods=["GET"])
def get_jobs():
    conn = get_db_connection()
    jobs = conn.execute("SELECT * FROM jobs ORDER BY id DESC").fetchall()
    conn.close()
    # Convert each row into a normal dictionary so it can be sent as JSON
    return jsonify([dict(job) for job in jobs])


# CREATE: add a new job application
@app.route("/api/jobs", methods=["POST"])
def add_job():
    data = request.get_json()

    company = data.get("company")
    role = data.get("role")
    date_applied = data.get("date_applied")
    status = data.get("status", "Applied")
    notes = data.get("notes", "")

    if not company or not role:
        return jsonify({"error": "Company and Role are required"}), 400

    conn = get_db_connection()
    conn.execute(
        "INSERT INTO jobs (company, role, date_applied, status, notes) VALUES (?, ?, ?, ?, ?)",
        (company, role, date_applied, status, notes)
    )
    conn.commit()
    conn.close()
    return jsonify({"message": "Job added successfully"}), 201


# UPDATE: change the status (or other fields) of a job application
@app.route("/api/jobs/<int:job_id>", methods=["PUT"])
def update_job(job_id):
    data = request.get_json()
    status = data.get("status")

    conn = get_db_connection()
    conn.execute("UPDATE jobs SET status = ? WHERE id = ?", (status, job_id))
    conn.commit()
    conn.close()
    return jsonify({"message": "Job updated successfully"})


# DELETE: remove a job application
@app.route("/api/jobs/<int:job_id>", methods=["DELETE"])
def delete_job(job_id):
    conn = get_db_connection()
    conn.execute("DELETE FROM jobs WHERE id = ?", (job_id,))
    conn.commit()
    conn.close()
    return jsonify({"message": "Job deleted successfully"})


if __name__ == "__main__":
    init_db()
    app.run(debug=True)
