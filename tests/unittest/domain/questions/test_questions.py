import unittest

from src.domain.questions.question import Question
from src.domain.questions.questions import Questions


class TestQuestions(unittest.TestCase):
    def setUp(self):
        self.questions = Questions()

    def test_register_a_new_question(self):
        theme = 'Test Theme'
        text = 'Test Text'
        options = ['Option1', 'Option2', 'Option3']
        correct_answer = 'Option2'

        self.questions.register_a_new_question(
            theme, text, options, correct_answer
        )

        self.assertEqual(len(self.questions.get_questions()), 1)
        new_question = self.questions.get_questions()[0]
        self.assertIsInstance(new_question, Question)
        self.assertEqual(new_question.get_theme(), theme)
        self.assertEqual(new_question.get_text(), text)
        self.assertEqual(new_question.get_options(), options)
        self.assertEqual(new_question.get_correct_answer(), correct_answer)

    def test_remove_a_question(self):
        questions = Questions()
        theme = 'Test Theme'
        text = 'Test removed'
        options = ['Option1', 'Option2', 'Option3']
        correct_answer = 'Option2'

        questions.register_a_new_question(
            theme, text, options, correct_answer
        )
        question_id = questions.get_questions()[0].get_question_id()

        questions.remove_a_question(question_id)

        self.assertEqual(len(questions.get_questions()), 0)

    def test_get_questions_by_theme_and_limit(self):
        theme = 'Test New Theme'
        limit = 2

        for i in range(5):
            self.questions.register_a_new_question(
                theme, f'Text {i}', ['Option1', 'Option2'], 'Option1'
            )

        questions_result = self.questions.get_questions_by_theme_and_limit(
            theme, limit
        )

        self.assertIsInstance(questions_result, list)
        self.assertTrue(
            all(
                isinstance(question, Question) for question in questions_result
            )
        )
        self.assertEqual(len(questions_result), limit)
        self.assertTrue(
            all(question.get_theme() == theme for question in questions_result)
        )

    def test_get_questions_by_theme(self):
        questions = Questions()
        theme = "Test Theme"

        for i in range(5):
            questions.register_a_new_question(
                theme, f"Text {i}", ["Option1", "Option2"], "Option1"
            )

        questions_result = questions.get_questions_by_theme(theme)

        self.assertIsInstance(questions_result, list)
        self.assertTrue(all(isinstance(question, Question)
                        for question in questions_result))
        self.assertTrue(all(question.get_theme() ==
                        theme for question in questions_result))

    def test_get_questions_sorted(self):
        questions = Questions()
        limit = 3

        themes = ["Theme1", "Theme2", "Theme3", "Theme4", "Theme5"]
        for i in range(len(themes)):
            questions.register_a_new_question(
                themes[i], f"Text {i}", ["Option1", "Option2"], "Option1"
            )

        sorted_questions_result = questions.get_questions_sorted(limit)

        self.assertIsInstance(sorted_questions_result, list)
        self.assertTrue(all(isinstance(question, Question)
                        for question in sorted_questions_result))

        sorted_question_ids = [question.get_question_id()
                               for question in sorted_questions_result]
        self.assertEqual(sorted_question_ids, sorted(sorted_question_ids))

        self.assertEqual(len(sorted_questions_result), limit)

    def test_get_questions(self):
        questions = Questions()

        for i in range(5):
            questions.register_a_new_question(
                f"Theme{i}", f"Text {i}", ["Option1", "Option2"], "Option1"
            )

        all_questions_result = questions.get_questions()

        self.assertIsInstance(all_questions_result, list)
        self.assertTrue(all(isinstance(question, Question)
                        for question in all_questions_result))
        self.assertEqual(len(all_questions_result), 5)
