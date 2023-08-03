from tokenize import String
from sqlalchemy import ARRAY, Column, Text
from src.infrastructure.adapters.database import Model


class QuestionModel(Model):
    id: str = Column(String(36), primary_key=True)
    theme: str = Column(String(100), nullable=False)
    text: str = Column(Text(), nullable=False)
    options: list = Column(ARRAY(Text()), nullable=False)
    correct_answer: str = Column(Text(), nullable=False)

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
