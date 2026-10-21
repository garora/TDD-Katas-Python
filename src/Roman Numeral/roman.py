"""Roman Numeral kata implementation."""


_ROMAN_NUMERALS = (
    (1000, "M"),
    (900, "CM"),
    (500, "D"),
    (400, "CD"),
    (100, "C"),
    (90, "XC"),
    (50, "L"),
    (40, "XL"),
    (10, "X"),
    (9, "IX"),
    (5, "V"),
    (4, "IV"),
    (1, "I"),
)
_ROMAN_VALUES = {symbol: value for value, symbol in _ROMAN_NUMERALS}


def get_roman_numeral(number):
    """Return the canonical Roman numeral for a positive integer."""
    if isinstance(number, bool) or not isinstance(number, int) or number <= 0:
        raise TypeError(
            "The value you entered is invalid: {num} is not a positive integer.".format(num=number)
        )

    numeral = []
    remaining = number
    for value, symbol in _ROMAN_NUMERALS:
        repetitions, remaining = divmod(remaining, value)
        numeral.append(symbol * repetitions)
    return "".join(numeral)


def get_number_from_roman_numeral(numeral):
    """Return the integer represented by a canonical uppercase Roman numeral."""
    if not isinstance(numeral, str) or not numeral:
        raise TypeError("numeral must be a non-empty Roman numeral string")

    try:
        values = [_ROMAN_VALUES[symbol] for symbol in numeral]
    except KeyError as error:
        raise ValueError("numeral contains an invalid Roman symbol") from error

    number = 0
    for index, value in enumerate(values):
        if index + 1 < len(values) and value < values[index + 1]:
            number -= value
        else:
            number += value

    if get_roman_numeral(number) != numeral:
        raise ValueError("numeral must be in canonical Roman numeral form")
    return number