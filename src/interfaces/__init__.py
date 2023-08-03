from flask import Flask

from .api import api_bp


def init_blueprints(app: Flask):
    app.register_blueprint(api_bp, url_prefix='/api/v1')
