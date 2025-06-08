import unittest
from my_awesome_lib.math_tools import calculate_circle_area, calculate_rectangle_area, add_numbers

class TestMathUtils(unittest.TestCase):
    def test_calculate_circle_area_positive(self):
        self.assertAlmostEqual(calculate_circle_area(2), 12.56636)
        self.assertAlmostEqual(calculate_circle_area(10), 314.159)
        self.assertAlmostEqual(calculate_circle_area(1), 3.14159)

    def test_calculate_circle_area_zero(self):
        self.assertEqual(calculate_circle_area(0), 0)

    def test_calculate_circle_area_negative(self):
        with self.assertRaises(ValueError):
            calculate_circle_area(-1)
        with self.assertRaises(ValueError):
            calculate_circle_area(-5.5)

    def test_calculate_rectangle_area_positive(self):
        self.assertAlmostEqual(calculate_rectangle_area(2, 3), 6.0)
        self.assertAlmostEqual(calculate_rectangle_area(5.5, 2), 11.0)
        self.assertAlmostEqual(calculate_rectangle_area(10, 10), 100.0)

    def test_calculate_rectangle_area_zero(self):
        self.assertEqual(calculate_rectangle_area(0, 5), 0)
        self.assertEqual(calculate_rectangle_area(5, 0), 0)
        self.assertEqual(calculate_rectangle_area(0, 0), 0)

    def test_calculate_rectangle_area_negative(self):
        with self.assertRaises(ValueError):
            calculate_rectangle_area(-1, 5)
        with self.assertRaises(ValueError):
            calculate_rectangle_area(5, -1)
        with self.assertRaises(ValueError):
            calculate_rectangle_area(-1, -1)

    def test_add_numbers_positive(self):
        self.assertEqual(add_numbers(2, 3), 5)
        self.assertEqual(add_numbers(0.5, 1.5), 2.0)

    def test_add_numbers_negative(self):
        self.assertEqual(add_numbers(-2, 3), 1)
        self.assertEqual(add_numbers(-5, -5), -10)

    def test_add_numbers_zero(self):
        self.assertEqual(add_numbers(0, 0), 0)
        self.assertEqual(add_numbers(5, 0), 5)

if __name__ == "__main__":
    unittest.main()
