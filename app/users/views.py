from flask import Blueprint, render_template, redirect, url_for, request
from flask_login import login_required, current_user, login_user
from werkzeug.exceptions import NotFound
from werkzeug.security import generate_password_hash

from app.extensions import db
from app.forms.user import RegisterForm
from app.models import User

users = Blueprint(name="users",
                  import_name=__name__,
                  url_prefix="/users")


@users.route("/")
def get_list():
    user_items = User.query.all()
    return render_template("users/list.html", users=user_items)


@users.route("/<int:pk>")
@login_required
def profile(pk: int):
    user = User.query.filter_by(id=pk).one_or_none()
    if not user:
        raise NotFound(f"User with ID={pk} not found")
    return render_template("users/profile.html", user=user)


@users.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('users.profile', pk=current_user.id))

    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate_on_submit():
        if User.query.filter_by(email=form.email.data).count():
            form.email.errors.append("Email is not unique")
            return render_template("users/register.html", form=form)
        user = User(email=form.email.data,
                    first_name=form.first_name.data,
                    last_name=form.last_name.data,
                    password=generate_password_hash(form.password.data))
        db.session.add(user)
        db.session.commit()
        login_user(user)

    return render_template("users/register.html", form=form)
