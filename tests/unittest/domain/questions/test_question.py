import unittest

from src.domain.questions.question import Question


class TestQuestion(unittest.TestCase):
    def test_get_question_id(self):
        question = Question(
            '1', 'Theme', 'Text', ['Option1', 'Option2'], 'Option1'
        )

        self.assertEqual(question.get_question_id(), '1')

    def test_get_theme(self):
        question = Question(
            '1', 'Theme', 'Text', ['Option1', 'Option2'], 'Option1'
        )

        self.assertEqual(question.get_theme(), 'Theme')
