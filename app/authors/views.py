from flask import Blueprint, render_template
from werkzeug.exceptions import NotFound

from app.models import Author

authors = Blueprint(name="authors",
                    import_name=__name__,
                    url_prefix="/authors")


@authors.route("/")
def get_list():
    authors = Author.query.all()
    return render_template("authors/list.html", authors=authors)


@authors.route("/<int:pk>")
def profile(pk: int):
    author = Author.query.filter_by(id=pk).one_or_none()
    if not author:
        raise NotFound(f"Author with ID={pk} not found")
    return render_template("authors/profile.html", author=authors)
