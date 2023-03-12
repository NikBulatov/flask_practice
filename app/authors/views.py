from flask import Blueprint, render_template
from app.models import Author

authors = Blueprint(name="authors",
                    import_name=__name__,
                    url_prefix="/authors")


@authors.route("/", endpoint="list")
def get_list():
    author_items = Author.query.all()
    return render_template("authors/list.html", authors=author_items)
