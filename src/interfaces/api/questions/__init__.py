from flask import Blueprint

from src.interfaces.api.questions.questions_controller import (
    QuestionsController,
)


def init_routes(api_bp: Blueprint):
    api_bp.add_url_rule(
        '/questions',
        view_func=QuestionsController().get_questions,
        methods=['GET'],
    )

    api_bp.add_url_rule(
        '/questions',
        view_func=QuestionsController.register_a_new_question,
        methods=['POST'],
    )

    api_bp.add_url_rule(
        '/questions',
        view_func=QuestionsController.remove_a_question,
        methods=['DELETE'],
    )

    api_bp.add_url_rule(
        '/questions/<string:theme>',
        view_func=QuestionsController.get_questions_by_theme,
        methods=['GET'],
    )

    api_bp.add_url_rule(
        '/questions/<string:theme>/<int:limit>',
        view_func=QuestionsController.get_questions_by_theme_and_limit,
        methods=['GET'],
    )

    api_bp.add_url_rule(
        '/questions/<int:limit>',
        view_func=QuestionsController.get_questions_sorted,
        methods=['GET'],
    )
