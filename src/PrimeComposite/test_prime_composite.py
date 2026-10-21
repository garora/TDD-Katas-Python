import unittest

from prime_composite import classify, classify_range


class PrimeCompositeTests(unittest.TestCase):
    def test_one_is_returned_unchanged(self):
        self.assertEqual(1, classify(1))

    def test_prime_numbers_are_classified_as_prime(self):
        self.assertEqual("Prime", classify(2))
        self.assertEqual("Prime", classify(3))
        self.assertEqual("Prime", classify(5))

    def test_odd_composites_are_classified_as_composite(self):
        self.assertEqual("Composite", classify(9))

    def test_even_composites_are_returned_unchanged(self):
        self.assertEqual(4, classify(4))

    def test_values_below_two_are_returned_unchanged(self):
        self.assertEqual(0, classify(0))
        self.assertEqual(-1, classify(-1))

    def test_default_range_covers_one_through_one_hundred(self):
        values = classify_range()

        self.assertEqual(100, len(values))
        self.assertEqual(1, values[0])
        self.assertEqual("Prime", values[1])
        self.assertEqual(4, values[3])
        self.assertEqual("Composite", values[8])

    def test_custom_range_is_inclusive(self):
        self.assertEqual(["Prime", 4, "Prime", 6, "Prime", 8, "Composite"], classify_range(3, 9))

    def test_non_integer_input_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "number must be an integer"):
            classify("9")

    def test_range_with_descending_bounds_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "start must not be greater"):
            classify_range(2, 1)


if __name__ == "__main__":
    unittest.main()