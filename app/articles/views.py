from flask import Blueprint, render_template
from werkzeug.exceptions import NotFound
import json

articles = Blueprint(name="articles",
                     import_name=__name__,
                     url_prefix="/articles")


@articles.route("/")
def get_list():
    with open("article_data.json", "r", encoding="utf-8") as f:
        articles = json.load(f)
        return render_template("articles/list.html", articles=articles)


@articles.route("/<int:pk>")
def get_item(pk: int):
    try:
        with open("article_data.json", "r", encoding="utf-8") as f:
            data = json.load(f)
            article = data[str(pk)]
    except KeyError:
        raise NotFound(f"Article with ID={pk} not found")
    return render_template("articles/details.html", article=article)
