from abc import ABC, abstractmethod

from src.application.dtos.question_dto import QuestionDTO


class QuestionsServicesInterface(ABC):
    @abstractmethod
    def register_a_new_question(self, data: QuestionDTO) -> None:
        pass

    @abstractmethod
    def remove_a_question(self, data: QuestionDTO) -> None:
        pass

    @abstractmethod
    def get_questions(self) -> list[QuestionDTO]:
        pass

    @abstractmethod
    def get_questions_by_theme_and_limit(
        self, data: QuestionDTO
    ) -> list[QuestionDTO]:
        pass

    @abstractmethod
    def get_questions_by_theme(self, data: QuestionDTO) -> list[QuestionDTO]:
        pass

    @abstractmethod
    def get_questions_sorted(self, data: QuestionDTO) -> list[QuestionDTO]:
        pass
