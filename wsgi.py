from app.app import create_app
from app.db import db
from app.models import Author

app = create_app()


@app.cli.command("init_db")
def init_db():
    db.create_all()


@app.cli.command("create_users")
def create_users():
    admin = Author(username="admin", is_staff=True, password="admin")
    james = Author(username="james", password="james")
    db.session.add(admin)
    db.session.add(james)
    db.session.commit()


if __name__ == "__main__":
    app.run(
        host="localhost",
        debug=True
    )
