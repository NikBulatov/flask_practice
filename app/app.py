from flask import Flask
from app.articles.views import articles
from app.followers.views import followers


def create_app() -> Flask:
    app = Flask(__name__)
    register_blueprints(app)
    return app


def register_blueprints(app: Flask) -> None:
    app.register_blueprint(articles)
    app.register_blueprint(followers)
