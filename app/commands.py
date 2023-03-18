import click
from werkzeug.security import generate_password_hash
from app.extensions import db


@click.command("create_users")
def create_users():
    from wsgi import app
    from app.models import User

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


@click.command("create_tags")
def create_tags():
    from wsgi import app
    from app.models import Tag

    with app.app_context():
        for name in ("art", "science", "culture", "photography"):
            db.session.add(Tag(name=name))
        db.session.commit()
