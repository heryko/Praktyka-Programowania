import unittest
from calculator import Add

class TestStringCalculator(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(Add(""), 0)

    def test_one_number(self):
        self.assertEqual(Add("1"), 1)

    def test_two_numbers(self):
        self.assertEqual(Add("1,2"), 3)

    def test_multiple_numbers(self):
        self.assertEqual(Add("1,2,3,4,5"), 15)

    def test_value_error_on_invalid_input(self):
        with self.assertRaises(ValueError):
            Add("1,nie_liczba,3")

    def test_newline_separator(self):
        self.assertEqual(Add("1\n2,3"), 6)

    def test_invalid_separator_sequence(self):
        with self.assertRaises(ValueError):
            Add("1,\n")

if __name__ == '__main__':
    unittest.main()