from flask import Response, jsonify, request

from src.application.contracts.questions_repository_interface import (
    QuestionsRepositoryInterface,
)
from src.application.contracts.questions_service_interface import (
    QuestionsServicesInterface,
)
from src.application.dtos.question_dto import QuestionDTO
from src.application.services.questions_service_impl import (
    QuestionsServiceImpl,
)
from src.infrastructure.repositories.questions_repository_impl import (
    QuestionsRepositoryImpl,
)
from src.interfaces.adapters.dict_to_object import DictToObject


class QuestionsController:
    repository: QuestionsRepositoryInterface = QuestionsRepositoryImpl()
    services: QuestionsServicesInterface = QuestionsServiceImpl(
        repository=repository
    )
    dto: QuestionDTO

    @classmethod
    def register_a_new_question(cls) -> Response:
        try:
            data_request = DictToObject(request.json)
            cls.dto = QuestionDTO(
                theme=data_request.theme,
                text=data_request.text,
                options=data_request.questions,
                correct_answer=data_request.correct_answer,
            )
            cls.services.register_a_new_question(cls.dto)
            return jsonify({'message': 'question registered'})
        except Exception as error:
            return jsonify({'error': '{}'.format(error)})

    @classmethod
    def remove_a_question(cls) -> Response:
        try:
            data_request = DictToObject(request.json)
            cls.dto = QuestionDTO(theme=data_request.id)
            cls.services.remove_a_question(cls.dto)
            return jsonify({'message': 'question removed'})
        except Exception as error:
            return jsonify({'error': '{}'.format(error)})

    @classmethod
    def get_questions(cls) -> Response:
        try:
            questions = cls.services.get_questions()
            return jsonify({'data': questions})
        except Exception as error:
            return jsonify({'error': '{}'.format(error)})

    @classmethod
    def get_questions_by_theme(cls, theme: str) -> Response:
        try:
            questions = cls.services.get_questions_by_theme(theme)
            return jsonify({'data': questions})
        except Exception as error:
            return jsonify({'error': '{}'.format(error)})

    @classmethod
    def get_questions_by_theme_and_limit(
        cls, theme: str, limit: int
    ) -> Response:
        try:
            questions = cls.services.get_questions_by_theme_and_limit(
                theme, limit
            )
            return jsonify({'data': questions})
        except Exception as error:
            return jsonify({'error': '{}'.format(error)})

    @classmethod
    def get_questions_sorted(cls, limit: int) -> Response:
        try:
            questions = cls.services.get_questions_sorted(limit)
            return jsonify({'limit': questions})
        except Exception as error:
            return jsonify({'error': '{}'.format(error)})
