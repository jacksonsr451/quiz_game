class QuestionDTO:
    id: str
    theme: str
    text: str
    options: list
    correct_answer: str
    limit: int

    def __init__(
        self,
        id: str = '',
        theme: str = '',
        text: str = '',
        options: list = '',
        correct_answer: str = '',
        limit: int = 0,
    ) -> None:
        self.id = id
        self.theme = theme
        self.text = text
        self.options = options
        self.correct_answer = correct_answer
        self.limit = limit
