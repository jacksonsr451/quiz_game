from uuid import uuid4

from src.infrastructure.models.question_model import QuestionModel


class TestQuestionModel:
    def test_should_create_question(self, session):
        question = QuestionModel(
            id=uuid4().__str__(),
            theme='Theme Test',
            text='This is a test question',
            options=['option1', 'option2'],
            correct_answer='option1',
        )
        session.add(question)
        session.commit()

        result = (
            session.query(QuestionModel).filter_by(id=question.id).first()
        )

        assert result is not None
        assert result.id == question.id
        assert result.theme == 'Theme Test'
        assert result.text == 'This is a test question'
        assert result.options == ['option1', 'option2']
        assert result.correct_answer == 'option1'
