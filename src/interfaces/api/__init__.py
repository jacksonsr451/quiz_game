from flask import Blueprint

from src.interfaces.api import questions

api_bp = Blueprint('api', __name__)

questions.init_routes(api_bp)
