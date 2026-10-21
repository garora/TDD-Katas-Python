import unittest

from calc_stats import calculate_stats


class CalcStatsTests(unittest.TestCase):
    def test_single_value_has_same_minimum_maximum_and_average(self):
        stats = calculate_stats([7])

        self.assertEqual(7, stats.minimum)
        self.assertEqual(7, stats.maximum)
        self.assertEqual(1, stats.count)
        self.assertEqual(7.0, stats.average)

    def test_positive_values(self):
        stats = calculate_stats([1, 2, 3, 4])

        self.assertEqual((1, 4, 4), (stats.minimum, stats.maximum, stats.count))
        self.assertEqual(2.5, stats.average)

    def test_negative_values(self):
        stats = calculate_stats([-5, -1, -3])

        self.assertEqual((-5, -1, 3), (stats.minimum, stats.maximum, stats.count))
        self.assertEqual(-3.0, stats.average)

    def test_mixed_values(self):
        stats = calculate_stats([-2, 0, 8])

        self.assertEqual((-2, 8, 3), (stats.minimum, stats.maximum, stats.count))
        self.assertEqual(2.0, stats.average)

    def test_catalog_example(self):
        stats = calculate_stats([6, 9, 15, -2, 92, 11])

        self.assertEqual(-2, stats.minimum)
        self.assertEqual(92, stats.maximum)
        self.assertEqual(6, stats.count)
        self.assertAlmostEqual(21.8333333333, stats.average)

    def test_empty_input_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "at least one"):
            calculate_stats([])

    def test_non_integer_values_are_rejected(self):
        with self.assertRaisesRegex(TypeError, "integers"):
            calculate_stats([1, 2.5, 3])

    def test_boolean_values_are_rejected(self):
        with self.assertRaisesRegex(TypeError, "integers"):
            calculate_stats([True, 2])

    def test_non_iterable_input_is_rejected(self):
        with self.assertRaisesRegex(TypeError, "iterable"):
            calculate_stats(42)


if __name__ == "__main__":
    unittest.main()