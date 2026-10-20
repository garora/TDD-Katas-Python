import unittest

from string_sum import sum_strings


class StringSumTests(unittest.TestCase):
    def test_empty_strings_sum_to_zero(self):
        self.assertEqual("0", sum_strings("", ""))

    def test_natural_number_strings_are_added(self):
        self.assertEqual("3", sum_strings("1", "2"))

    def test_invalid_left_value_is_treated_as_zero(self):
        self.assertEqual("2", sum_strings("not a number", "2"))

    def test_invalid_right_value_is_treated_as_zero(self):
        self.assertEqual("1", sum_strings("1", "not a number"))

    def test_negative_number_string_is_treated_as_zero(self):
        self.assertEqual("1", sum_strings("1", "-2"))

    def test_non_string_values_are_treated_as_zero(self):
        self.assertEqual("0", sum_strings(None, None))

    def test_leading_zeroes_are_normalized_in_the_result(self):
        self.assertEqual("10", sum_strings("007", "003"))


if __name__ == "__main__":
    unittest.main()