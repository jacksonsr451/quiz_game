from uuid import uuid4

from src.domain.questions import question
from src.domain.questions.question import Question


class Questions:
    __questions_list: list[Question]

    def __init__(self, questions: list = []) -> None:
        self.__questions_list = [question for question in questions]

    def register_a_new_question(
        self,
        theme: str,
        text: str,
        options: list,
        correct_answer: str,
    ) -> Question:
        question = Question(
            question_id=self.__get_id(),
            theme=theme,
            text=text,
            options=options,
            correct_answer=correct_answer,
        )
        self.__questions_list.append(question)
        return question

    def remove_a_question(self, question_id: str) -> None:
        if all(
            question.get_question_id() != question_id
            for question in self.__questions_list
        ):
            raise ValueError('Question not found')

        self.__questions_list = [
            question
            for question in self.__questions_list
            if question.get_question_id() != question_id
        ]

    def get_questions_by_theme_and_limit(
        self, theme: str, limit: int
    ) -> list[Question]:
        value: list = [
            question
            for question in sorted(
                self.__questions_list,
                key=lambda question: question.get_question_id(),
            )
            if question.get_theme() == theme
        ]
        return value[:limit]

    def get_questions_by_theme(self, theme: str) -> list[Question]:
        return [
            question
            for question in self.__questions_list
            if question.get_theme() == theme
        ]

    def get_questions_sorted(self, limit: int) -> list[Question]:
        return sorted(
            self.__questions_list,
            key=lambda question: question.get_question_id(),
        )[:limit]

    def get_questions(self) -> list[Question]:
        return self.__questions_list

    def __get_id(self) -> str:
        return uuid4().__str__()
