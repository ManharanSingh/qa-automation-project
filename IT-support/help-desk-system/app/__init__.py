import re
from sqlalchemy import or_
from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
    abort,
)
from flask_sqlalchemy import SQLAlchemy



db = SQLAlchemy()

def create_app(test_config=None):
    app = Flask(__name__)

    app.config.from_mapping(
        SQLALCHEMY_DATABASE_URI="sqlite:///helpdesk.db",
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
    )

    if test_config:
        app.config.update(test_config)

    db.init_app(app)

    from app.models import Ticket

    with app.app_context():
        db.create_all()

    @app.route("/", methods=["GET", "POST"])
    def home():
        if request.method == "POST":
            user_name = request.form.get("user_name", "").strip()
            user_email = request.form.get("user_email", "").strip()
            title = request.form.get("title", "").strip()
            description = request.form.get("description", "").strip()
            category = request.form.get("category", "").strip()
            priority = request.form.get("priority", "Medium").strip()

           # Validate required fields
            if not all([
              user_name,
              user_email,
              title,
              description,
              category,
              ]):
                abort(400, description="All required fields must be filled.")

            # Validate maximum lengths
            if (
                 len(user_name) > 100
                 or len(user_email) > 150
                 or len(title) > 150
                 or len(description) > 5000
                 ):
                abort(400, description="One or more fields exceed the allowed length.")

            # Basic email format validation
            if not re.fullmatch(r"[^@\s]+@[^@\s]+\.[^@\s]+", user_email):
                abort(400, description="Invalid email format.")

            # Allow only recognised categories and priorities
            allowed_categories = {
                "Hardware",
                "Software",
                "Network",
                "Account",
                "Security",
                "Other",
                }

            allowed_priorities = {
                "Low",
                "Medium",
                "High",
                "Critical",
                }

            if category not in allowed_categories:
                abort(400, description="Invalid ticket category.")

            if priority not in allowed_priorities:
                abort(400, description="Invalid ticket priority.")

            ticket = Ticket(
                user_name=user_name,
                user_email=user_email,
                title=title,
                description=description,
                category=category,
                priority=priority,
                )

            db.session.add(ticket)
            db.session.commit()

            return redirect(
                url_for("tickets_details", ticket_id=ticket.id)
                )
        
        return render_template("create_ticket.html")

    
    @app.route("/tickets")
    def tickets():
        search = request.args.get("search", "").strip()
        status_filter = request.args.get("status", "").strip()
        priority_filter = request.args.get("priority", "").strip()

        allowed_statuses = {
            "Open",
            "In Progress",
            "Resolved",
            "Closed",
            }

        allowed_priorities = {
            "Low",
            "Medium",
            "High",
            "Critical",
            }

        if status_filter and status_filter not in allowed_statuses:
            abort(400, description="Invalid status filter.")

        if priority_filter and priority_filter not in allowed_priorities:
            abort(400, description="Invalid priority filter.")

        query = Ticket.query

        # Search by ticket ID, title, requester, email, or description
        if search:
            pattern = f"%{search}%"

            conditions = [
                Ticket.title.ilike(pattern),
                Ticket.user_name.ilike(pattern),
                Ticket.user_email.ilike(pattern),
                Ticket.description.ilike(pattern),
            ]

            if search.isdigit():
                conditions.append(Ticket.id == int(search))

            query = query.filter(or_(*conditions))

        # Apply selected filters
        if status_filter:
            query = query.filter(Ticket.status == status_filter)

        if priority_filter:
            query = query.filter(Ticket.priority == priority_filter)

        all_tickets = query.order_by(
            Ticket.created_at.desc()
            ).all()

        return render_template(
            "tickets.html",
            tickets=all_tickets,
            search=search,
            status_filter=status_filter,
            priority_filter=priority_filter,
            )

    @app.route("/tickets/<int:ticket_id>",
    methods = ["GET", "POST"])
    def tickets_details(ticket_id):
        ticket = db.get_or_404(Ticket, ticket_id)

        if request.method == "POST":
            status = request.form.get("status", "").strip()
            technician = request.form.get("technician", "").strip()
            notes = request.form.get("notes", "").strip()

            allowed_statuses = {
                "Open",
                "In Progress",
                "Resolved",
                "Closed",
                }

            # Validate status
            if status not in allowed_statuses:
                abort(400, description="Invalid ticket status.")

            # Validate technician name length
            if len(technician) > 100:
                abort(400, description="Technician name is too long.")

            # Limit troubleshooting notes
            if len(notes) > 5000:
                abort(400, description="Troubleshooting notes are too long.")

            ticket.status = status
            ticket.technician = technician or None
            ticket.notes = notes or None

            db.session.commit()

            return redirect(url_for(
                "tickets_details",
                ticket_id=ticket.id
            ))

        return render_template(
            "ticket_details.html",
            ticket=ticket
        )
    
    return app
    
