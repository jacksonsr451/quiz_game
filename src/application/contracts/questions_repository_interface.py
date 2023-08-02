from abc import ABC, abstractmethod

from src.infrastructure.models.question_model import QuestionModel


class QuestionsRepositoryInterface(ABC):
    @abstractmethod
    def register(self, model) -> None:
        pass

    @abstractmethod
    def remove(self, question_id: str) -> None:
        pass

    @abstractmethod
    def get_all(self) -> list[QuestionModel]:
        pass
