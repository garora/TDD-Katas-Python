# TDD Katas - Python Practice Guide

This guide adapts the exercise-oriented approach of the companion TDD-Katas repository to the Python code and tests available here. Only the two katas currently present in `src` are documented below.

## Contents

- [Practicing TDD](#practicing-tdd)
- [Recently Used List](#recently-used-list)
- [Roman Numeral](#roman-numeral)
- [Running the Tests](#running-the-tests)
- [Contributing](#contributing)

## Practicing TDD

Work through each kata in small steps:

1. **Red:** Write a test for one new behavior and run it to confirm that it fails for the expected reason.
2. **Green:** Write the smallest amount of code that makes the test pass.
3. **Refactor:** Improve the implementation and tests without changing their behavior, keeping the tests green.
4. Repeat with the next example or edge case.

The existing implementations are practice material, not a guarantee that every behavior described below is already implemented. Optional challenges are deliberately separated from current behavior.

## Recently Used List

**Implementation:** [rul.py](src/Recently%20Used%20List/rul.py)

**Tests:** [test_rul.py](src/Recently%20Used%20List/test_rul.py)

### Goal

Develop a `RecentlyUsedList` class that stores unique strings in most-recently-used order.

### Core Requirements

- A new list is empty.
- The most recently inserted item is first; the least recently inserted item is last.
- Items can be retrieved by a zero-based index.
- Inserting an existing item moves it to the front instead of adding a duplicate.
- `len(recently_used_list)` returns the number of unique items.

### Suggested Test Progression

1. Create a list and verify that its length is zero.
2. Insert one item and retrieve it at index `0`.
3. Insert two different items and verify their order.
4. Insert a duplicate and verify both its new position and the unchanged length.
5. Check the ordering of the remaining items after moving an older item to the front.
6. Verify that accessing an index beyond the list raises `IndexError`.

For example, inserting `"a"`, `"b"`, `"c"`, and then `"b"` should leave the items in the order `"b"`, `"c"`, `"a"`.

### Optional Challenges

Adapted from the reference guide; these are not implemented as explicit policies in the current class:

- Reject `None` and empty strings, with a clearly documented exception type.
- Add a configurable capacity and discard the least recently used item on overflow.
- Consider a default capacity of five while allowing an explicitly unbounded list.
- Reject negative indexes if that is the contract you choose. The current implementation delegates indexing to a Python list, so negative indexes currently work.
- Test the valid index range carefully: a list with `n` items has non-negative indexes from `0` through `n - 1`.

## Roman Numeral

**Implementation:** [roman.py](src/Roman%20Numeral/roman.py)

**Tests:** [roman_test.py](src/Roman%20Numeral/roman_test.py)

### Goal

Practice converting positive integers to Roman numerals with `get_roman_numeral(number)`. The repository also contains a work-in-progress reverse converter, `get_number_from_roman_numeral(numeral)`.

### Conversion Rules

| Symbol | Value |
| --- | ---: |
| I | 1 |
| V | 5 |
| X | 10 |
| L | 50 |
| C | 100 |
| D | 500 |
| M | 1000 |

Combine symbols additively, using the subtractive pairs `IV`, `IX`, `XL`, `XC`, `CD`, and `CM` where appropriate.

| Integer | Roman numeral |
| ---: | --- |
| 1 | I |
| 7 | VII |
| 9 | IX |
| 34 | XXXIV |
| 448 | CDXLVIII |
| 1989 | MCMLXXXIX |
| 2444 | MMCDXLIV |

### Suggested Test Progression

1. Start with the single-symbol values `1`, `5`, and `10`.
2. Add repeated and combined symbols, such as `2`, `7`, and `16`.
3. Introduce subtractive notation, starting with `4` and `9`.
4. Extend to tens, hundreds, and thousands, testing each subtractive boundary.
5. Test mixed values such as `448` and `1989`.
6. Reject zero, negative numbers, and non-integer inputs. Existing tests expect `TypeError` for invalid inputs.
7. Complete the reverse converter, beginning with `I`, `V`, and `X`, then additive and subtractive combinations.

### Current Limitations and Optional Challenges

- `roman.py` contains Python 2 syntax and APIs, including bare `print` statements and `long`. It cannot currently be imported by Python 3; porting it is a useful follow-up exercise.
- The reverse converter is unfinished. Its string normalization and indexing need attention before its tests can pass reliably.
- Two integer-to-Roman tests share the method name `test_four`; the later definition replaces the earlier one. Give tests unique names so both cases run.
- Decide and test a policy for lowercase numerals, empty input, and invalid Roman numeral sequences.
- Decide and test an upper bound. Existing tests include `5494 -> MMMMMCDXCIV`, so do not assume the current exercise is restricted to `1` through `3999`.
- Once both conversions work, add round-trip tests: converting an integer to Roman numerals and back should return the original integer.

## Running the Tests

The test files use Python's built-in `unittest` framework; they do not require a third-party test runner. Run these commands from the repository root:

```powershell
# Recently Used List
python -m unittest discover -s "src/Recently Used List" -p "test_rul.py" -v

# Roman Numeral (requires porting roman.py before it can run on Python 3)
python -m unittest discover -s "src/Roman Numeral" -p "roman_test.py" -v
```

Use separate discovery commands because the kata directories contain spaces, are not Python packages, and use different test filename conventions. The Roman Numeral command currently fails on Python 3 because of the legacy syntax described above; that is an existing limitation, not an additional dependency to install.

## Contributing

Add focused tests, explain the behavior being introduced, and keep code changes scoped to the kata you are practicing. Submit pull requests against `develop`, not `master`.

See [README.md](README.md) for project information, related implementations, and contributor acknowledgements, and [LICENSE](LICENSE) for the MIT license.
