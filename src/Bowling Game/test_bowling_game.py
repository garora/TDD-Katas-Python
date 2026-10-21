import unittest

from bowling_game import BowlingGame


class BowlingGameTests(unittest.TestCase):
    def setUp(self):
        self.game = BowlingGame()

    def test_gutter_game_scores_zero(self):
        self._roll_many(0, 20)
        self.assertEqual(0, self.game.score())

    def test_all_ones_scores_twenty(self):
        self._roll_many(1, 20)
        self.assertEqual(20, self.game.score())

    def test_spare_adds_the_next_roll_as_a_bonus(self):
        self._roll(5, 5, 3)
        self._roll_many(0, 17)
        self.assertEqual(16, self.game.score())

    def test_strike_adds_the_next_two_rolls_as_a_bonus(self):
        self._roll(10, 3, 4)
        self._roll_many(0, 16)
        self.assertEqual(24, self.game.score())

    def test_final_frame_spare_uses_its_bonus_roll(self):
        self._roll_many(0, 18)
        self._roll(5, 5, 7)
        self.assertEqual(17, self.game.score())

    def test_final_frame_strike_uses_its_two_bonus_rolls(self):
        self._roll_many(0, 18)
        self._roll(10, 3, 4)
        self.assertEqual(17, self.game.score())

    def test_perfect_game_scores_three_hundred(self):
        self._roll_many(10, 12)
        self.assertEqual(300, self.game.score())

    def test_invalid_roll_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "between 0 and 10"):
            self.game.roll(11)

    def _roll(self, *pins):
        for pin_count in pins:
            self.game.roll(pin_count)

    def _roll_many(self, pins, rolls):
        for _ in range(rolls):
            self.game.roll(pins)


if __name__ == "__main__":
    unittest.main()