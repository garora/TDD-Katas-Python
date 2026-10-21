"""Tests for the Roman Numeral kata."""

import unittest

from roman import get_number_from_roman_numeral, get_roman_numeral


class RomanNumeralsConvertToRomanTests(unittest.TestCase):
    def test_individual_symbols(self):
        self.assertEqual("I", get_roman_numeral(1))
        self.assertEqual("V", get_roman_numeral(5))
        self.assertEqual("X", get_roman_numeral(10))
        self.assertEqual("L", get_roman_numeral(50))
        self.assertEqual("C", get_roman_numeral(100))
        self.assertEqual("D", get_roman_numeral(500))
        self.assertEqual("M", get_roman_numeral(1000))

    def test_additive_values(self):
        self.assertEqual("VII", get_roman_numeral(7))
        self.assertEqual("XVI", get_roman_numeral(16))
        self.assertEqual("XXVIII", get_roman_numeral(28))
        self.assertEqual("LXXXVIII", get_roman_numeral(88))

    def test_subtractive_values(self):
        self.assertEqual("IV", get_roman_numeral(4))
        self.assertEqual("IX", get_roman_numeral(9))
        self.assertEqual("XL", get_roman_numeral(40))
        self.assertEqual("XC", get_roman_numeral(90))
        self.assertEqual("CD", get_roman_numeral(400))
        self.assertEqual("CM", get_roman_numeral(900))

    def test_larger_values(self):
        self.assertEqual("CDXLVIII", get_roman_numeral(448))
        self.assertEqual("MCMLXXXIX", get_roman_numeral(1989))
        self.assertEqual("MMMMMCDXCIV", get_roman_numeral(5494))

    def test_non_positive_and_non_integer_values_are_rejected(self):
        for value in (-1, 0, None, "", "test", True):
            with self.subTest(value=value):
                with self.assertRaises(TypeError):
                    get_roman_numeral(value)

    def test_invalid_value_message_is_clear(self):
        with self.assertRaises(TypeError) as error:
            get_roman_numeral("test")
        self.assertEqual(
            "The value you entered is invalid: test is not a positive integer.",
            str(error.exception),
        )


class RomanNumeralsConvertToNumberFromRomanTests(unittest.TestCase):
    def test_individual_symbols(self):
        self.assertEqual(1, get_number_from_roman_numeral("I"))
        self.assertEqual(5, get_number_from_roman_numeral("V"))
        self.assertEqual(10, get_number_from_roman_numeral("X"))
        self.assertEqual(50, get_number_from_roman_numeral("L"))

    def test_subtractive_values(self):
        self.assertEqual(4, get_number_from_roman_numeral("IV"))
        self.assertEqual(9, get_number_from_roman_numeral("IX"))
        self.assertEqual(1990, get_number_from_roman_numeral("MCMXC"))

    def test_round_trip_conversion(self):
        for number in (1, 4, 9, 39, 448, 1989, 5494):
            with self.subTest(number=number):
                self.assertEqual(number, get_number_from_roman_numeral(get_roman_numeral(number)))

    def test_invalid_roman_numerals_are_rejected(self):
        for numeral in ("", "A", "IIII", "IC", "VX", None):
            with self.subTest(numeral=numeral):
                with self.assertRaises((TypeError, ValueError)):
                    get_number_from_roman_numeral(numeral)


if __name__ == "__main__":
    unittest.main()