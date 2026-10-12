
# IT Help Desk Ticketing System

A Flask-based IT Help Desk application that demonstrates common IT support ticket workflows, database management, server-side validation, and automated testing.

## Overview

This project simulates a basic internal IT support system where users can submit technical issues and technicians can review tickets, assign ownership, update status, and document troubleshooting notes.

The goal is to demonstrate practical Python development and an understanding of IT service desk operations.

## Features

- Create support tickets with requester information and issue details.
- Store tickets persistently using SQLite and SQLAlchemy.
- View ticket details, including category, priority, status, and creation time.
- Assign a technician and update the ticket status.
- Record troubleshooting notes.
- Search tickets by ID, title, requester name, email, or description.
- Filter tickets by status and priority.
- Display the newest tickets first.
- Validate submitted data on the server.
- Use automated tests to verify core functionality.

## Technology Stack

- **Language:** Python
- **Web framework:** Flask
- **Database:** SQLite
- **ORM:** Flask-SQLAlchemy
- **Frontend:** HTML and CSS
- **Templating:** Jinja2
- **Testing:** pytest

## Ticket Workflow

1. A requester submits an IT support ticket.
2. The application validates the submitted information.
3. The ticket is saved to the SQLite database.
4. The user is redirected to the ticket details page.
5. A technician can review the ticket, assign a technician, update its status, and record troubleshooting notes.
6. The dashboard can be used to search and filter tickets.

## Project Structure

```text
IT-Help-Desk/
├── app/
│   ├── __init__.py
│   ├── models.py
│   └── templates/
│       ├── create_ticket.html
│       ├── tickets.html
│       └── ticket_details.html
├── tests/
│   └── test_tickets.py
├── run.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Setup and Installation

### 1. Clone the repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd IT-Help-Desk
```

Replace the placeholder with the actual repository URL.

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

On Linux or macOS:

```bash
source .venv/bin/activate
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Run the application

```bash
python run.py
```

Open the local address:

http://127.0.0.1:5000

## Automated Tests

Run the test suite with:

```bash
python -m pytest -q
```

The current test suite covers:

- Successful ticket creation.
- Rejection of an invalid ticket category.
- Rejection of an invalid status update.
- Filtering tickets by priority.

Tests use an in-memory SQLite database to avoid modifying the local application database.

## Skills Demonstrated

- Python application development
- Flask routing and application structure
- Relational data modeling
- SQLite and SQLAlchemy
- HTML forms and Jinja2 templates
- Backend input validation
- Database querying and filtering
- Automated testing with pytest
- Troubleshooting and iterative development

## Project Scope

This is a learning and portfolio project intended for local demonstration. It does not currently implement user authentication or role-based access control and is not intended for public production deployment.

## Future Improvements

- Ticket activity history
- Dashboard pagination
- More comprehensive automated tests
- Improved reporting and ticket metrics
