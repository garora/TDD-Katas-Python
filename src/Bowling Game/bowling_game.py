"""Bowling Game kata implementation."""


class BowlingGame:
    """Record bowling rolls and calculate the score for a ten-frame game."""

    def __init__(self):
        self._rolls = []

    def roll(self, pins):
        """Record the number of pins knocked down in one roll."""
        if isinstance(pins, bool) or not isinstance(pins, int) or not 0 <= pins <= 10:
            raise ValueError("pins must be an integer between 0 and 10")
        self._rolls.append(pins)

    def score(self):
        """Return the score after processing ten frames and any bonus rolls."""
        score = 0
        roll_index = 0

        for _ in range(10):
            if self._is_strike(roll_index):
                score += 10 + self._rolls[roll_index + 1] + self._rolls[roll_index + 2]
                roll_index += 1
            elif self._is_spare(roll_index):
                score += 10 + self._rolls[roll_index + 2]
                roll_index += 2
            else:
                score += self._rolls[roll_index] + self._rolls[roll_index + 1]
                roll_index += 2

        return score

    def _is_strike(self, roll_index):
        return self._rolls[roll_index] == 10

    def _is_spare(self, roll_index):
        return self._rolls[roll_index] + self._rolls[roll_index + 1] == 10