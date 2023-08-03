from flask import jsonify, request


class QuestionsController:
    @staticmethod
    def register_a_new_question():
        data = request.get_json()
        return jsonify(data)
