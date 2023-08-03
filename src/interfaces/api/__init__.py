from flask import Blueprint

from src.interfaces.api.questions_controller import QuestionsController

api_bp = Blueprint('api', __name__)


api_bp.add_url_rule(
    '/questions',
    view_func=QuestionsController.register_a_new_question,
    methods=['POST'],
)
