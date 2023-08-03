from flask import Response, jsonify, request


class QuestionsController:
    @staticmethod
    def register_a_new_question() -> Response:
        data = request.get_json()
        return jsonify(data)

    @staticmethod
    def remove_a_question() -> Response:
        return jsonify({'message': 'question removed'})

    @staticmethod
    def get_questions() -> Response:
        return jsonify({'data': 'all questions'})

    @staticmethod
    def get_questions_by_theme(theme: str) -> Response:
        return jsonify({'theme': theme})

    @staticmethod
    def get_questions_by_theme_and_limit(theme: str, limit: int) -> Response:
        return jsonify({"theme": theme, "limit": limit})

    @staticmethod
    def get_questions_sorted(limit: int) -> Response:
        return jsonify({'limit': limit})
