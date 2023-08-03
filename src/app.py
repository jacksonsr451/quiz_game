from flask import Flask

from src import interfaces
from src.infrastructure.adapters import database


def start_app() -> Flask:
    app = Flask(__name__)
    return app


def create_app() -> Flask:
    app = start_app()
    database.init_app(app)

    interfaces.init_blueprints(app)
    return app
