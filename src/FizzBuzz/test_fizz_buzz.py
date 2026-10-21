import unittest

from fizz_buzz import fizz_buzz, fizz_buzz_range


class FizzBuzzTests(unittest.TestCase):
    def test_an_ordinary_number_is_returned_unchanged(self):
        self.assertEqual(1, fizz_buzz(1))

    def test_a_multiple_of_three_returns_fizz(self):
        self.assertEqual("Fizz", fizz_buzz(3))

    def test_a_multiple_of_five_returns_buzz(self):
        self.assertEqual("Buzz", fizz_buzz(5))

    def test_a_multiple_of_three_and_five_returns_fizzbuzz(self):
        self.assertEqual("FizzBuzz", fizz_buzz(15))

    def test_default_range_covers_one_through_one_hundred(self):
        values = fizz_buzz_range()

        self.assertEqual(100, len(values))
        self.assertEqual(1, values[0])
        self.assertEqual("Fizz", values[2])
        self.assertEqual("Buzz", values[4])
        self.assertEqual("FizzBuzz", values[14])
        self.assertEqual("Buzz", values[-1])

    def test_custom_range_is_inclusive(self):
        self.assertEqual(["Fizz", 4, "Buzz", "Fizz", 7], fizz_buzz_range(3, 7))

    def test_non_integer_input_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "number must be an integer"):
            fizz_buzz("3")

    def test_range_with_descending_bounds_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "start must not be greater"):
            fizz_buzz_range(2, 1)


if __name__ == "__main__":
    unittest.main()