"""OddEven kata implementation."""


def classify(number):
    """Classify an integer as ``"Even"``, ``"Odd"``, or leave it unchanged.

    Prime numbers and values below 2 are returned unchanged. Positive
    non-prime even numbers return ``"Even"``; positive odd composites return
    ``"Odd"``.
    """
    _validate_integer(number, "number")

    if number < 2 or _is_prime(number):
        return number
    if number % 2 == 0:
        return "Even"
    return "Odd"


def classify_range(start=1, end=100):
    """Return classifications for all integers in an inclusive range."""
    _validate_integer(start, "start")
    _validate_integer(end, "end")
    if start > end:
        raise ValueError("start must not be greater than end")

    return [classify(number) for number in range(start, end + 1)]


def _is_prime(number):
    if number < 2:
        return False

    divisor = 2
    while divisor * divisor <= number:
        if number % divisor == 0:
            return False
        divisor += 1
    return True


def _validate_integer(value, name):
    if isinstance(value, bool) or not isinstance(value, int):
        raise ValueError(f"{name} must be an integer")