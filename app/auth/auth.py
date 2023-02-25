from flask import redirect, url_for, Blueprint
from app.models import Author
from flask_login import LoginManager

__all__ = [
    "login_manager",
    "auth",
]
login_manager = LoginManager()
login_manager.login_view = "auth.login"

auth = Blueprint(name="auth",
                 import_name=__name__,
                 url_prefix="/auth")


@login_manager.user_loader
def load_user(id):
    return Author.query.filter_by(id=id).one_or_none()


@login_manager.unauthorized_handler
def unauthorized():
    return redirect(url_for("auth.login"))
