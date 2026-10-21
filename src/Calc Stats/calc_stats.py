"""Calc Stats kata implementation."""

from typing import NamedTuple


class Statistics(NamedTuple):
    """Summary statistics for an iterable of integers."""

    minimum: int
    maximum: int
    count: int
    average: float


def calculate_stats(values):
    """Return minimum, maximum, count, and arithmetic average for ``values``.

    ``values`` may be any iterable of integers. Empty iterables raise
    ``ValueError``; non-iterables and non-integer elements raise ``TypeError``.
    Boolean values are rejected even though ``bool`` is an ``int`` subclass.
    """
    try:
        iterator = iter(values)
    except TypeError:
        raise TypeError("values must be an iterable of integers") from None

    try:
        first = next(iterator)
    except StopIteration:
        raise ValueError("values must contain at least one integer") from None

    _validate_integer(first)
    minimum = maximum = total = first
    count = 1

    for value in iterator:
        _validate_integer(value)
        minimum = min(minimum, value)
        maximum = max(maximum, value)
        total += value
        count += 1

    return Statistics(minimum, maximum, count, total / count)


def _validate_integer(value):
    if isinstance(value, bool) or not isinstance(value, int):
        raise TypeError("values must contain only integers")