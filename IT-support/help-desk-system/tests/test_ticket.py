import pytest

from app import create_app, db
from app.models import Ticket


@pytest.fixture
def app():
    app = create_app({
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:",
    })

    yield app

    with app.app_context():
        db.session.remove()
        db.drop_all()


@pytest.fixture
def client(app):
    return app.test_client()


def ticket_data(**overrides):
    data = {
        "user_name": "Alice",
        "user_email": "alice@example.com",
        "title": "Wi-Fi not working",
        "description": "Laptop cannot connect to Wi-Fi.",
        "category": "Network",
        "priority": "Medium",
    }

    data.update(overrides)
    return data


def test_create_ticket(client, app):
    response = client.post("/", data=ticket_data())

    assert response.status_code == 302
    assert response.headers["Location"].endswith("/tickets/1")

    with app.app_context():
        ticket = db.session.get(Ticket, 1)

        assert ticket is not None
        assert ticket.title == "Wi-Fi not working"
        assert ticket.status == "Open"


def test_reject_invalid_category(client, app):
    response = client.post(
        "/",
        data=ticket_data(category="SuperAdmin"),
    )

    assert response.status_code == 400

    with app.app_context():
        assert Ticket.query.count() == 0


def test_reject_invalid_status(client, app):
    client.post("/", data=ticket_data())

    response = client.post(
        "/tickets/1",
        data={
            "status": "Hacked",
            "technician": "Bob",
            "notes": "Test update",
        },
    )

    assert response.status_code == 400

    with app.app_context():
        ticket = db.session.get(Ticket, 1)
        assert ticket.status == "Open"


def test_priority_filter(client):
    client.post(
        "/",
        data=ticket_data(
            title="VPN unavailable",
            priority="Critical",
        ),
    )

    client.post(
        "/",
        data=ticket_data(
            title="Mouse broken",
            priority="Low",
        ),
    )

    response = client.get("/tickets?priority=Critical")

    assert response.status_code == 200
    assert b"VPN unavailable" in response.data
    assert b"Mouse broken" not in response.data
