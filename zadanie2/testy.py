import unittest
from parameterized import parameterized
from app import (
    is_valid_email, calculate_circle_area,
    filter_even_numbers, convert_date_format, is_palindrome
)

class TestIsValidEmail(unittest.TestCase):
    @parameterized.expand([
        ("test@example.com",),
        ("another.one@domain.co.uk",),
        ("user123@sub.domain.net",),
        ("first.last@mail.com",),
        ("email@sub.domain.com",),
        ("12345@domain.com",),
        ("a@b.co",),
        ("test-dash@domain.com",)
    ])
    def test_valid_email(self, email):
        self.assertTrue(is_valid_email(email), f"Expected {email} to be valid")

    @parameterized.expand([
        ("invalid-email",),
        ("test@.com",),
        ("@example.com",),
        ("test@example",),
        ("test@example..com",),
        ("test@example.",),
        (".test@example.com",),
        ("test@example.com.",),
        ("test@example.c",),
        ("test@example,com",),
        ("test example@domain.com",),
        ("test@example_domain.com",),
        ("test@-example.com",),
    ])
    def test_invalid_email(self, email):
        self.assertFalse(is_valid_email(email), f"Expected {email} to be invalid")

    def test_email_with_numbers_and_hyphens(self):
        self.assertTrue(is_valid_email("john-doe123@example-mail.com"))


class TestCalculateCircleArea(unittest.TestCase):
    @parameterized.expand([
        (1, 3.141592653589793),
        (0, 0),
        (2, 12.566370614359172),
        (10, 314.1592653589793)
    ])
    def test_positive_radius(self, radius, expected_area):
        self.assertAlmostEqual(calculate_circle_area(radius), expected_area, places=10)

    def test_zero_radius(self):
        self.assertAlmostEqual(calculate_circle_area(0), 0)

    def test_negative_radius_raises_error(self):
        with self.assertRaises(ValueError) as cm:
            calculate_circle_area(-5)
        self.assertEqual(str(cm.exception), "Radius cannot be negative")

class TestFilterEvenNumbers(unittest.TestCase):
    @parameterized.expand([
        ([1, 2, 3, 4, 5, 6], [2, 4, 6]),
        ([], []),
        ([1, 3, 5], []),
        ([2, 4, 6], [2, 4, 6]),
        ([0, 1, 2, -4, 5, -6], [0, 2, -4, -6]),
        (['a', 2, 'b', 4, 5.5], [2, 4]),
        ([True, False, 2], [2]),
    ])
    def test_filter_even_numbers(self, input_list, expected_list):
        self.assertEqual(filter_even_numbers(input_list), expected_list)

class TestConvertDateFormat(unittest.TestCase):
    @parameterized.expand([
        ("01-01-2024", "2024/01/01"),
        ("31-12-1999", "1999/12/31"),
        ("29-02-2024", "2024/02/29"),
        ("15-06-2000", "2000/06/15"),
    ])
    def test_correct_date_format_conversion(self, input_date, expected_date):
        self.assertEqual(convert_date_format(input_date), expected_date)

    @parameterized.expand([
        ("2024-01-01",),
        ("01/01/2024",),
        ("32-01-2024",),
        ("01-13-2024",),
        ("01-01-202",),
        ("invalid-date",),
        ("",),
        ("29-02-2023",)
    ])
    def test_incorrect_date_format_raises_value_error(self, invalid_date_str):
        with self.assertRaises(ValueError) as cm:
            convert_date_format(invalid_date_str)
        self.assertIn("Incorrect date format", str(cm.exception))


class TestIsPalindrome(unittest.TestCase):
    @parameterized.expand([
        ("Kajak",),
        ("A man, a plan, a canal: Panama",),
        ("Madam",),
        ("Racecar",),
        ("No lemon, no melon",),
        ("refer",),
        ("",),
        ("A",),
        ("  ",),
        ("abacaba",),
    ])
    def test_is_palindrome_true(self, text):
        self.assertTrue(is_palindrome(text), f"Expected '{text}' to be a palindrome")

    @parameterized.expand([
        ("Hello",),
        ("Python",),
        ("Not a palindrome",),
    ])
    def test_is_palindrome_false(self, text):
        self.assertFalse(is_palindrome(text), f"Expected '{text}' to not be a palindrome")

    def test_is_palindrome_with_numbers(self):
        self.assertTrue(is_palindrome("12321"))
        self.assertFalse(is_palindrome("12345"))

    def test_is_palindrome_with_special_chars(self):
        self.assertTrue(is_palindrome("!@#Madam!@#"))
        self.assertFalse(is_palindrome("abc!@#def"))

if __name__ == "__main__":
    unittest.main()
