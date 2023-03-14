from flask import render_template, request, redirect, url_for, Blueprint
from flask_login import login_user, login_required, logout_user, current_user
from werkzeug.security import check_password_hash

from app.forms.auth import LoginForm
from app.models import User

__all__ = ['auth']

auth = Blueprint(name="auth",
                 import_name=__name__,
                 url_prefix="/auth")


@auth.route("/login", methods=["POST", "GET"], endpoint="login")
def login():
    form = LoginForm(request.form)

    if request.method == "GET":
        if current_user.is_authenticated:
            return redirect(url_for('users.profile', pk=current_user.id))
        return render_template('auth/login.html', form=form)

    if request.method == "POST" and form.validate_on_submit():
        email = request.form.get("email")
        password = request.form.get('password')

        user = User.query.filter_by(email=email).one_or_none()

        if not user or not check_password_hash(user.password, password):
            form.email.errors.append("Check your email")
            form.password.errors.append("Check your password")
            render_template("auth/login.html", form=form,
                            error=f"Check your login details")

        login_user(user)
        return redirect(url_for("users.profile", pk=user.id))


@auth.route("/logout/", endpoint="logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("users.list"))
