"""String Sum kata implementation."""


def sum_strings(left, right):
    """Return the sum of two natural-number strings as a string.

    Values that are not strings containing decimal digits are treated as zero.
    """
    return str(_natural_number_or_zero(left) + _natural_number_or_zero(right))


def _natural_number_or_zero(value):
    """Convert a natural-number string to ``int``; otherwise return zero."""
    if isinstance(value, str) and value.isdecimal():
        return int(value)
    return 0