import unittest

from prime_factors import prime_factors


class PrimeFactorTests(unittest.TestCase):
    def test_one_has_no_prime_factors(self):
        self.assertEqual([], prime_factors(1))

    def test_prime_numbers_return_themselves(self):
        self.assertEqual([2], prime_factors(2))
        self.assertEqual([3], prime_factors(3))

    def test_four_has_two_repeated_factors(self):
        self.assertEqual([2, 2], prime_factors(4))

    def test_six_has_two_distinct_factors(self):
        self.assertEqual([2, 3], prime_factors(6))

    def test_eight_preserves_repeated_factors(self):
        self.assertEqual([2, 2, 2], prime_factors(8))

    def test_twelve_has_repeated_and_distinct_factors(self):
        self.assertEqual([2, 2, 3], prime_factors(12))

    def test_a_larger_composite_is_factored_in_ascending_order(self):
        self.assertEqual([3, 3, 5, 7], prime_factors(315))

    def test_zero_and_negative_numbers_are_rejected(self):
        with self.assertRaisesRegex(ValueError, "positive integer"):
            prime_factors(0)
        with self.assertRaisesRegex(ValueError, "positive integer"):
            prime_factors(-1)

    def test_non_integer_input_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "positive integer"):
            prime_factors("12")


if __name__ == "__main__":
    unittest.main()