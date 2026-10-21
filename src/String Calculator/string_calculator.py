"""String Calculator kata implementation."""

import re


def add(numbers):
    """Return the sum of the numbers in a delimiter-separated string.

    The default separators are commas and newlines.  A custom delimiter can
    be declared with ``//<delimiter>\n``; the legacy ``<delimiter>\n`` form
    from this repository's kata catalog is also accepted.

    Raises:
        ValueError: If one or more supplied values are negative.
    """
    if numbers == "":
        return 0

    delimiters, number_list = _delimiters_and_numbers(numbers)
    values = [int(value) for value in re.split(_separator_pattern(delimiters), number_list)]

    negatives = [value for value in values if value < 0]
    if negatives:
        negative_values = ", ".join(str(value) for value in negatives)
        raise ValueError(f"negatives not allowed: {negative_values}")

    return sum(values)


def _delimiters_and_numbers(numbers):
    """Extract a declared delimiter, when present, and the numeric portion."""
    if numbers.startswith("//"):
        delimiter, number_list = numbers[2:].split("\n", 1)
        return [delimiter], number_list

    first_line, separator, number_list = numbers.partition("\n")
    if separator and len(first_line) == 1 and not first_line.isdigit() and first_line != ",":
        return [first_line], number_list

    return [",", "\n"], numbers


def _separator_pattern(delimiters):
    """Build a regular expression that treats each delimiter literally."""
    return "|".join(re.escape(delimiter) for delimiter in delimiters)