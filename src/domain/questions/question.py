class Question:
    __question_id: str
    __theme: str
    __text: str
    __options: list
    __correct_answer: str

    def __init__(
        self,
        question_id: str,
        theme: str,
        text: str,
        options: list,
        correct_answer: str,
    ) -> None:
        self.__question_id = question_id
        self.__theme = theme
        self.__text = text
        self.__options = options
        self.__correct_answer = correct_answer

    def get_question_id(self) -> str:
        return self.__question_id

    def get_theme(self) -> str:
        return self.__theme

    def get_theme(self) -> str:
        return self.__theme

    def get_text(self) -> str:
        return self.__text

    def get_options(self) -> list:
        return self.__options

    def get_correct_answer(self) -> str:
        return self.__correct_answer
