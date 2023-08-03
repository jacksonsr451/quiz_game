from flask import Flask

from src.infrastructure.adapters.database import db


def start_app() -> Flask:
    app = Flask(__name__)
    return app


def create_app() -> Flask:
    app = start_app()
    db.init_app(app)

    return app
