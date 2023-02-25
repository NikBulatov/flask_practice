from flask import Flask
from app.articles.views import articles
from app.auth.auth import login_manager
from app.authors.views import authors
from app.auth.views import auth
from app.db import db
from config import Config


def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    login_manager.init_app(app)
    register_blueprints(app)
    return app


def register_blueprints(app: Flask) -> None:
    app.register_blueprint(articles)
    app.register_blueprint(authors)
    app.register_blueprint(auth)
