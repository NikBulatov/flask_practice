from flask import Blueprint, render_template, redirect, url_for, request
from flask_login import login_required, current_user, login_user
from werkzeug.exceptions import NotFound
from werkzeug.security import generate_password_hash

from app.extensions import db
from app.forms.author import RegisterForm
from app.models import Author

authors = Blueprint(name="authors",
                    import_name=__name__,
                    url_prefix="/authors")


@authors.route("/")
def get_list():
    authors = Author.query.all()
    return render_template("authors/list.html", authors=authors)


@authors.route("/<int:pk>")
@login_required
def profile(pk: int):
    author = Author.query.filter_by(id=pk).one_or_none()
    if not author:
        raise NotFound(f"Author with ID={pk} not found")
    return render_template("authors/profile.html", author=author)


@authors.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('authors.profile', pk=current_user.id))

    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate_on_submit():
        if Author.query.filter_by(email=form.email.data).count():
            form.email.errors.append("Email is not unique")
            return render_template("authors/register.html", form=form)
        author = Author(email=form.email.data,
                        first_name=form.first_name.data,
                        last_name=form.last_name.data,
                        password=generate_password_hash(form.password.data))
        db.session.add(author)
        db.session.commit()
        login_user(author)

    return render_template("authors/register.html", form=form)
