#  Job Application Tracker
**Live Demo:** https://jobapplication-ipeg.onrender.com

A simple fullstack web app to track job applications — company, role, status
(Applied / Interview / Offer / Rejected), and notes.

## Tech Stack
- **Backend:** Python, Flask
- **Database:** SQLite
- **Frontend:** HTML, CSS, JavaScript (fetch API)

## Features
- Add a new job application
- View all applications in a table
- Update application status from a dropdown
- Delete an application

## How to Run Locally

1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Run the app:
   ```
   python app.py
   ```

3. Open your browser and go to:
   ```
   http://127.0.0.1:5000
   ```

The SQLite database file (`jobs.db`) is created automatically the first time
you run the app.

## Project Structure
```
job-tracker/
│
├── app.py              # Flask backend (routes + database logic)
├── requirements.txt    # Python dependencies
├── templates/
│   └── index.html      # Main webpage
└── static/
    ├── style.css        # Styling
    └── script.js         # Frontend logic (talks to the backend API)
```

## What This Project Demonstrates
- Building REST API endpoints (GET, POST, PUT, DELETE)
- Connecting a frontend to a backend using `fetch()`
- Storing and retrieving data with SQLite
- Basic fullstack app structure (frontend + backend + database)
