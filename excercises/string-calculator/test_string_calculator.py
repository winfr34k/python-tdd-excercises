import unittest
import string_calculator


class StringCalculatorAddTestCase(unittest.TestCase):
    def assertResultIsCorrect(self, string_of_numbers, expected_result):
        self.assertEquals(string_calculator.add(string_of_numbers), expected_result)

    def assertStringContains(self, haystack, needle):
        self.assertIn(needle, str(haystack))

    def test_returns_zero_on_empty_string(self):
        self.assertResultIsCorrect("", 0)

    def test_returns_number_when_single_number_is_given(self):
        self.assertResultIsCorrect("1", 1)

    def test_one_plus_two(self):
        self.assertResultIsCorrect("1,2", 3)

    def test_three_plus_four(self):
        self.assertResultIsCorrect("3,4", 7)

    def test_one_plus_zero(self):
        self.assertResultIsCorrect("1,0", 1)

    def test_one_plus_zero_plus_ten(self):
        self.assertResultIsCorrect("1,0,10", 11)

    def test_trailing_comma_is_not_an_issue(self):
        self.assertResultIsCorrect("1,", 1)

    def test_support_for_newline_delimiter(self):
        self.assertResultIsCorrect("1\n0,10", 11)

    def test_support_for_custom_delimiter(self):
        self.assertResultIsCorrect("//;\n1;2", 3)

    def test_support_for_custom_delimiter_of_variable_length(self):
        self.assertResultIsCorrect("//;;;\n1;;;2", 3)

    def test_support_for_slash_as_custom_delimiter(self):
        self.assertResultIsCorrect("///\n1/2", 3)

    def test_exception_on_negative_numbers(self):
        with self.assertRaises(string_calculator.NegativeNumbersException):
            string_calculator.add("-1,-2")

    def test_exception_on_negative_numbers_has_correct_message(self):
        with self.assertRaises(string_calculator.NegativeNumbersException) as raised:
            string_calculator.add("-1,-2")

        self.assertStringContains(raised.exception, "negatives not allowed")

    def test_exception_on_negative_numbers_contains_numbers(self):
        with self.assertRaises(string_calculator.NegativeNumbersException) as raised:
            string_calculator.add("-1,-2")

        self.assertEquals(raised.exception.negative_numbers, [-1, -2])