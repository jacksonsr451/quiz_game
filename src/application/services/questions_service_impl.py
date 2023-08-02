from src.application.contracts.questions_repository_interface import (
    QuestionsRepositoryInterface,
)
from src.application.contracts.questions_service_interface import (
    QuestionsServicesInterface,
)
from src.application.dtos.question_dto import QuestionDTO
from src.domain.questions.question import Question
from src.domain.questions.questions import Questions
from src.infrastructure.models.question_model import QuestionModel


class QuestionsServiceImpl(QuestionsServicesInterface):
    repository: QuestionsRepositoryInterface
    questions: Questions

    def __init__(self, repository: QuestionsRepositoryInterface):
        self.repository = repository
        self.questions = Questions(self.repository.get_questions())

    def register_a_new_question(self, data: QuestionDTO) -> None:
        question = self.questions.register_a_new_question(
            data.text, data.theme, data.options, data.correct_answer
        )
        self.repository.register(self.__question_to_model(question))

    def remove_a_question(self, data: QuestionDTO) -> None:
        self.questions.remove_a_question(data.question_id)
        self.repository.remove(data.id)

    def get_questions(self) -> list[QuestionDTO]:
        questions = self.questions.get_questions()
        return self.__list_questions_to_dto(questions)

    def get_questions_by_theme(self, data: QuestionDTO) -> list[QuestionDTO]:
        questions = self.questions.get_questions_by_theme(data.theme)
        return self.__list_questions_to_dto(questions)

    def get_questions_by_theme_and_limit(
        self, data: QuestionDTO
    ) -> list[QuestionDTO]:
        questions = self.questions.get_questions_by_theme_and_limit(
            data.theme, data.limit
        )
        return self.__list_questions_to_dto(questions)

    def get_questions_sorted(self, data: QuestionDTO) -> list[QuestionDTO]:
        questions = self.questions.get_questions_sorted(data.limit)
        return self.__list_questions_to_dto(questions)

    def __question_to_model(self, question: Question) -> QuestionModel:
        return QuestionModel(
            question.get_question_id(),
            question.get_theme(),
            question.get_text(),
            question.get_options(),
            question.get_correct_answer(),
        )

    def __list_questions_to_dto(
        self, questions: list[Question]
    ) -> list[QuestionDTO]:
        return [
            QuestionDTO(
                question.get_question_id(),
                question.get_theme(),
                question.get_text(),
                question.get_options(),
                question.get_correct_answer(),
            )
            for question in questions
        ]
