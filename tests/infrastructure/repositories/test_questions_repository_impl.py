from uuid import uuid4

import pytest

from src.infrastructure.models.question_model import QuestionModel
from src.infrastructure.repositories.questions_repository_impl import (
    QuestionsRepositoryImpl,
)


class TestQuestionsRepositoryImpl:
    @pytest.fixture(scope='function')
    def questions_repository_impl(self, session):
        return QuestionsRepositoryImpl(session=session)

    def test_register_question(self, questions_repository_impl, session):
        question = QuestionModel(
            id=uuid4().__str__(),
            theme='Theme Test',
            text='This is a test question',
            options=['option1', 'option2'],
            correct_answer='option1',
        )

        questions_repository_impl.register(model=question)

        result = session.query(QuestionModel).filter_by(id=question.id).first()
        assert result is not None
        assert result.theme == 'Theme Test'
        assert result.text == 'This is a test question'
        assert result.options == ['option1', 'option2']
        assert result.correct_answer == 'option1'

    def test_remove_question(self, session):
        question_id = uuid4().__str__()
        question = QuestionModel(
            id=question_id,
            theme='Theme Test',
            text='This is a test question',
            options='["option1", "option2"]',
            correct_answer='option1',
        )
        session.add(question)
        session.commit()
        repository = QuestionsRepositoryImpl(session)

        repository.remove(question_id)

        result = session.query(QuestionModel).filter_by(id=question_id).first()
        assert result is None

    def test_get_all_questions(self, questions_repository_impl):
        question1 = QuestionModel(
            id=uuid4().__str__(),
            theme='Theme Test 1',
            text='This is a test question 1',
            options='["option1", "option2"]',
            correct_answer='option1',
        )
        question2 = QuestionModel(
            id=uuid4().__str__(),
            theme='Theme Test 2',
            text='This is a test question 2',
            options='["option3", "option4"]',
            correct_answer='option3',
        )

        questions_repository_impl.register(model=question1)
        questions_repository_impl.register(model=question2)

        questions = questions_repository_impl.get_all()

        assert len(questions) == 2
        assert questions[0].theme == 'Theme Test 1'
        assert questions[1].theme == 'Theme Test 2'
        assert questions[0].text == 'This is a test question 1'
        assert questions[1].text == 'This is a test question 2'
        assert questions[0].options == '["option1", "option2"]'
        assert questions[1].options == '["option3", "option4"]'
        assert questions[0].correct_answer == 'option1'
        assert questions[1].correct_answer == 'option3'
