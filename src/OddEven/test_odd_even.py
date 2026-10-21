import unittest

from odd_even import classify, classify_range


class OddEvenTests(unittest.TestCase):
    def test_one_is_returned_unchanged(self):
        self.assertEqual(1, classify(1))

    def test_prime_numbers_are_returned_unchanged(self):
        self.assertEqual(2, classify(2))
        self.assertEqual(3, classify(3))
        self.assertEqual(5, classify(5))

    def test_positive_even_non_prime_numbers_are_classified_as_even(self):
        self.assertEqual("Even", classify(4))

    def test_odd_composite_numbers_are_classified_as_odd(self):
        self.assertEqual("Odd", classify(9))

    def test_values_below_two_are_returned_unchanged(self):
        self.assertEqual(0, classify(0))
        self.assertEqual(-1, classify(-1))

    def test_default_range_covers_one_through_one_hundred(self):
        values = classify_range()

        self.assertEqual(100, len(values))
        self.assertEqual(1, values[0])
        self.assertEqual(2, values[1])
        self.assertEqual("Even", values[3])
        self.assertEqual("Odd", values[8])

    def test_custom_range_is_inclusive(self):
        self.assertEqual([3, "Even", 5, "Even", 7, "Even", "Odd"], classify_range(3, 9))

    def test_non_integer_input_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "number must be an integer"):
            classify("9")

    def test_range_with_descending_bounds_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "start must not be greater"):
            classify_range(2, 1)


if __name__ == "__main__":
    unittest.main()