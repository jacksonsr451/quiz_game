from flask_sqlalchemy import SQLAlchemy
from src.application.contracts.questions_repository_interface import QuestionsRepositoryInterface
from src.infrastructure.models.question_model import QuestionModel


class QuestionsRepositoryImpl(QuestionsRepositoryInterface):
    db: SQLAlchemy

    def __init__(self, db: SQLAlchemy) -> None:
        self.db = db

    def register(self, model: QuestionModel) -> None:
        self.db.session.add(model)
        self.db.session.commit()

    def remove(self, question_id: str) -> None:
        question = self.db.session.query(
            QuestionModel).filter_by(id=question_id).first()
        self.db.session.delete(question)
        self.db.session.commit()

    def get_all(self) -> list[QuestionModel]:
        return self.db.session.query(QuestionModel).all()
