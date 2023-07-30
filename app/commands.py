import click
from werkzeug.security import generate_password_hash

from app.extensions import db


@click.command("create-init-user")
def create_init_user():
    from app.models import User
    from wsgi import app

    with app.app_context():
        db.session.add(
            User(
                email="ex@ex.com",
                password=generate_password_hash("123"),
                is_staff=True,
            )
        )
        db.session.commit()


@click.command("create-init-tags")
def create_init_tags():
    from app.models import Tag
    from wsgi import app

    with app.app_context():
        tags = ("flask", "django", "python", "gb", "sqlite")
        for item in tags:
            db.session.add(Tag(name=item))
        db.session.commit()
    click.echo(f'Created tags: {", ".join(tags)}')
