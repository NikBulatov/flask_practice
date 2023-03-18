from flask import (Blueprint,
                   render_template,
                   request, current_app,
                   url_for,
                   redirect)
from flask_login import current_user, login_required
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import joinedload
from werkzeug.exceptions import NotFound

from app.extensions import db
from app.forms import CreateArticleForm
from app.models import Article, Author, Tag

articles = Blueprint(name="articles",
                     import_name=__name__,
                     url_prefix="/articles")


@articles.route("/", endpoint="list")
def get_list():
    article_items = Article.query.all()
    return render_template("articles/list.html", articles=article_items)


@articles.route("/<int:pk>", endpoint="details")
def get_item(pk: int):
    article = Article.query.filter_by(id=pk).options(
        joinedload(Article.tags)).one_or_none()
    if not article:
        raise NotFound(f"Article with ID={pk} not found")
    return render_template("articles/details.html", article=article)


@articles.route("/create/", methods=["POST", "GET"], endpoint="create")
@login_required
def create_article():
    error = None
    form = CreateArticleForm(request.form)
    form.tags.choices = [(tag.id, tag.name) for tag in
                         Tag.query.order_by("name")]

    if request.method == "POST" and form.validate_on_submit():
        article = Article(title=form.title.data.strip(), body=form.body.data)
        if form.tags.data:
            selected_tags = Tag.query.filter(Tag.id.in_(form.tags.data))
            for tag in selected_tags:
                article.tags.append(tag)

        if current_user.author:
            article.author = current_user.author
        else:
            author = Author(user_id=current_user.id)
            db.session.add(author)
            db.session.flush()
            article.author = current_user.author

        try:
            db.session.add(article)
            db.session.commit()
        except IntegrityError:
            error = "Could not create a new article!"
            current_app.logger.exception(error)
        else:
            return redirect(url_for("articles.details", pk=article.id))

    return render_template("articles/create.html", form=form, error=error)
