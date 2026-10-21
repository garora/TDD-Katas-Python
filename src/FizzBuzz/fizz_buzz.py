"""FizzBuzz kata implementation."""


def fizz_buzz(number):
    """Return the FizzBuzz value for an integer.

    Multiples of three return ``"Fizz"``, multiples of five return
    ``"Buzz"``, and multiples of both return ``"FizzBuzz"``. All other
    integers are returned unchanged.
    """
    _validate_integer(number, "number")

    if number % 15 == 0:
        return "FizzBuzz"
    if number % 3 == 0:
        return "Fizz"
    if number % 5 == 0:
        return "Buzz"
    return number


def fizz_buzz_range(start=1, end=100):
    """Return FizzBuzz values for every integer in the inclusive range."""
    _validate_integer(start, "start")
    _validate_integer(end, "end")
    if start > end:
        raise ValueError("start must not be greater than end")

    return [fizz_buzz(number) for number in range(start, end + 1)]


def _validate_integer(value, name):
    if isinstance(value, bool) or not isinstance(value, int):
        raise ValueError(f"{name} must be an integer")