import unittest
from my_awesome_lib.data_utils import filter_even_numbers, convert_date_format, reverse_list

class TestDataUtils(unittest.TestCase):
    def test_filter_even_numbers(self):
        self.assertEqual(filter_even_numbers([1, 2, 3, 4]), [2, 4])
        self.assertEqual(filter_even_numbers([1, 3, 5]), [])
        self.assertEqual(filter_even_numbers([2, 'a', 4.5, 6]), [2, 6])

    def test_filter_even_numbers_empty_list(self):
        self.assertEqual(filter_even_numbers([]), [])

    def test_convert_date_format_valid(self):
        self.assertEqual(convert_date_format("01-01-2024"), "2024/01/01")
        self.assertEqual(convert_date_format("31-12-1999"), "1999/12/31")

    def test_convert_date_format_invalid(self):
        with self.assertRaises(ValueError):
            convert_date_format("2024/01/01")
        with self.assertRaises(ValueError):
            convert_date_format("abc")
        with self.assertRaises(ValueError):
            convert_date_format("01-JAN-2024")

    def test_reverse_list(self):
        self.assertEqual(reverse_list([1, 2, 3]), [3, 2, 1])
        self.assertEqual(reverse_list(['a', 'b', 'c']), ['c', 'b', 'a'])
        self.assertEqual(reverse_list([]), [])
        self.assertEqual(reverse_list([1]), [1])
        self.assertEqual(reverse_list([1, 2, 3, 4, 5]), [5, 4, 3, 2, 1])

if __name__ == "__main__":
    unittest.main()
