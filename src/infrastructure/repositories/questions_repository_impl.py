from flask_sqlalchemy import SQLAlchemy

from src.application.contracts.questions_repository_interface import (
    QuestionsRepositoryInterface,
)
from src.infrastructure.adapters.database import Session
from src.infrastructure.models.question_model import QuestionModel


class QuestionsRepositoryImpl(QuestionsRepositoryInterface):
    session: Session

    def __init__(self, session: Session) -> None:
        self.session = session

    def register(self, model: QuestionModel) -> None:
        self.session.add(model)
        self.session.commit()

    def remove(self, question_id: str) -> None:
        question = (
            self.session.query(QuestionModel).filter_by(id=question_id).first()
        )
        self.session.delete(question)
        self.session.commit()

    def get_all(self) -> list[QuestionModel]:
        return self.session.query(QuestionModel).all()
