from flask import Blueprint, render_template
from werkzeug.exceptions import NotFound

from app.models import Article

articles = Blueprint(name="articles",
                     import_name=__name__,
                     url_prefix="/articles")


@articles.route("/", endpoint="list")
def get_list():
    article_items = Article.query.all()
    return render_template("articles/list.html", articles=article_items)


@articles.route("/<int:pk>", endpoint="details")
def get_item(pk: int):
    article = Article.query.filter_by(id=pk).one_or_none()
    if not article:
        raise NotFound(f"Article with ID={pk} not found")
    return render_template("articles/details.html", article=article)
