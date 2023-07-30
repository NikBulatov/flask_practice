from combojsonapi.event import EventPlugin
from combojsonapi.permission import PermissionPlugin
from combojsonapi.spec import ApiSpecPlugin
from flask import Flask
from app import commands
from app.extensions import db, login_manager, migrate, csrf, admin, api
from app.models import User


def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object("app.config")

    register_extensions(app)
    register_blueprints(app)
    register_commands(app)
    return app


def register_extensions(app):
    db.init_app(app)
    migrate.init_app(app, db, compare_type=True)
    csrf.init_app(app)
    admin.init_app(app)
    api.plugins = [
        EventPlugin(),
        PermissionPlugin(),
        ApiSpecPlugin(
            app=app,
            tags={
                "Tag": "Tag API",
                "User": "User API",
                "Author": "Author API",
                "Article": "Article API",
            },
        ),
    ]
    api.init_app(app)

    login_manager.login_view = "auth.login"
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))


def register_blueprints(app: Flask):
    from app.auth.views import auth
    from app.user.views import user
    from app.author.views import author
    from app.articles.views import article
    from app.api.views import api_blueprint
    from app import admin

    app.register_blueprint(user)
    app.register_blueprint(auth)
    app.register_blueprint(author)
    app.register_blueprint(article)
    app.register_blueprint(api_blueprint)

    admin.register_views()


def register_commands(app: Flask):
    app.cli.add_command(commands.create_init_user)
    app.cli.add_command(commands.create_init_tags)
