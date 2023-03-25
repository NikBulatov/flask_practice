from flask import Flask, redirect, url_for
from app import commands
from app.api import api
from app.extensions import migrate, login_manager, db, csrf
from app.models import User
from app.views import admin
from app.views import auth
from app.views import articles
from app.views import users
from config import DevelopmentConfig


def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig)

    register_extensions(app)
    register_blueprints(app)
    register_commands(app)
    return app


def register_blueprints(app: Flask) -> None:
    app.register_blueprint(users)
    app.register_blueprint(auth)
    app.register_blueprint(articles)


def register_extensions(app: Flask) -> None:
    db.init_app(app)
    migrate.init_app(app, db, compare_type=True)
    admin.init_app(app)
    csrf.init_app(app)
    api.init_app(app)

    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    @login_manager.unauthorized_handler
    def unauthorized():
        return redirect(url_for("auth.login"))


def register_commands(app: Flask):
    app.cli.add_command(commands.create_users)
    app.cli.add_command(commands.create_tags)
