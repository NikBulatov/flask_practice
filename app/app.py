from flask import Flask
from app.object.views import object_item
from app.pages.views import page


# enter point
def create_app() -> Flask:
    app = Flask(__name__)
    register_blueprints(app)
    return app


def register_blueprints(app: Flask) -> None:
    app.register_blueprint(object_item)
    app.register_blueprint(page)
