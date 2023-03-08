from flask import Flask
from app.articles.views import articles
from app.auth.auth import login_manager
from app.authors.views import authors
from app.auth.views import auth
from app.db import db
from config import DevelopmentConfig


def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig)
    register_extensions(app)
    register_blueprints(app)
    return app


def register_blueprints(app: Flask) -> None:
    app.register_blueprint(articles)
    app.register_blueprint(authors)
    app.register_blueprint(auth)


def register_extensions(app: Flask) -> None:
    db.init_app(app)
    login_manager.init_app(app)
