import unittest
from my_awesome_lib.text_processing import is_palindrome, count_words


class TestTextProcessing(unittest.TestCase):
    def test_is_palindrome_true(self):
        self.assertTrue(is_palindrome("Kajak"))
        self.assertTrue(is_palindrome("A man, a plan, a canal: Panama"))
        self.assertTrue(is_palindrome("Racecar"))
        self.assertTrue(is_palindrome("madam"))

    def test_is_palindrome_false(self):
        self.assertFalse(is_palindrome("Hello"))
        self.assertFalse(is_palindrome("Python"))

    def test_is_palindrome_empty_string(self):
        self.assertTrue(is_palindrome(""))

    def test_is_palindrome_with_numbers(self):
        self.assertTrue(is_palindrome("121"))
        self.assertFalse(is_palindrome("1A2B1"))

    def test_count_words_basic(self):
        self.assertEqual(count_words("Hello world"), 2)
        self.assertEqual(count_words("This is a test sentence"), 5)

    def test_count_words_empty_string(self):
        self.assertEqual(count_words(""), 0)

    def test_count_words_leading_trailing_spaces(self):
        self.assertEqual(count_words("  Hello  world  "), 2)

    def test_count_words_multiple_spaces(self):
        self.assertEqual(count_words("One   two    three"), 3)

    def test_count_words_punctuation(self):
        self.assertEqual(count_words("Hello, world!"), 2)
        self.assertEqual(count_words("Hello-world"), 1)


if __name__ == "__main__":
    unittest.main()
