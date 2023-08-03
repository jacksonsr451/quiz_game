from flask import Flask, redirect, request

from .api import api_bp


def init_blueprints(app: Flask):
    app.register_blueprint(api_bp, url_prefix='/api/v1')

    @app.before_request
    def strip_trailing_slash():
        if request.path != '/' and request.path.endswith('/'):
            return redirect(request.path[:-1])
