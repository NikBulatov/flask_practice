import click
from werkzeug.security import generate_password_hash
from app.extensions import db
from app.models import User


@click.command("create_users")
def create_users():
    from wsgi import app

    with app.app_context():
        db.session.add(User(email="admin@ex.com", is_staff=True,
                            password=generate_password_hash("admin"),
                            first_name="admin",
                            last_name="adminov"))
        db.session.add(User(email="james@ex.com",
                            password=generate_password_hash("james"),
                            first_name="james",
                            last_name="jamesov"))

        db.session.commit()


@click.command("init_db")
def init_db():
    db.create_all()
