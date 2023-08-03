from sqlalchemy import JSON, Column, String, Text

from src.infrastructure.adapters.database import Base


class QuestionModel(Base):
    __tablename__ = 'questions'

    id = Column(String(36), primary_key=True)
    theme = Column(String, nullable=False)
    text = Column(String, nullable=False)
    options = Column(JSON, nullable=False)
    correct_answer = Column(String, nullable=False)

    def __init__(
        self,
        id: str,
        theme: str,
        text: str,
        options: list,
        correct_answer: str,
    ) -> None:
        self.id = id
        self.theme = theme
        self.text = text
        self.options = options
        self.correct_answer = correct_answer
