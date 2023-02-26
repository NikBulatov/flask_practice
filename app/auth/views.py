from flask import render_template, request, redirect, url_for, Blueprint
from flask_login import login_user, login_required, logout_user
from app.models import Author

__all__ = ['auth']

auth = Blueprint(name="auth",
                 import_name=__name__,
                 url_prefix="/auth")


@auth.route("/login", methods=["POST", "GET"], endpoint="login")
def login():
    if request.method == "GET":
        return render_template("auth/login.html")

    username = request.form.get("username")
    if not username:
        return render_template("auth/login.html", error="Username not passed")

    user = Author.query.filter_by(username=username).one_or_none()

    if not user:
        render_template("auth/login.html", error=f"no user {username!r}")

    login_user(user)

    return redirect(url_for("authors.profile", pk=user.id))


@auth.route("/logout/", endpoint="logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("authors.get_list"))
