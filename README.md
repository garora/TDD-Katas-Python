# TDD Katas - Python

## Description

A collection of Python Test-Driven Development (TDD) katas. Each kata is kept in its own directory under `src` with a standard-library `unittest` suite so it can be practiced independently.

## Requirements

- Python 3.10 or newer
- No third-party runtime or test dependencies

Check your Python version from the repository root:

```powershell
python --version
```

## Run the Tests

Run every implemented kata test suite from a clean checkout:

```powershell
python run_tests.py
```

The runner discovers test files in every kata directory, including directories whose names contain spaces, and returns a non-zero exit code if any test fails.

To run one kata suite, use its documented command. For example:

```powershell
python -m unittest discover -s "src/FizzBuzz" -p "test_fizz_buzz.py" -v
```

Individual test files can also be run directly when they provide a `unittest` entry point. For example:

```powershell
python "src/Roman Numeral/roman_test.py"
```

## Implemented Katas

- [Recently Used List](src/Recently%20Used%20List/)
- [String Sum](src/String%20Sum/)
- [String Calculator](src/String%20Calculator/)
- [Bowling Game](src/Bowling%20Game/)
- [FizzBuzz](src/FizzBuzz/)
- [OddEven](src/OddEven/)
- [Prime Factor](src/Prime%20Factor/)
- [Roman Numeral](src/Roman%20Numeral/)

The source-level guide contains kata-specific APIs, examples, and test commands: [src/README.md](src/README.md).

## Contributing

Contributions are welcome. Open pull requests against the [`develop`](https://github.com/garora/TDD-Katas-Python/tree/develop) branch rather than `master`. Report problems or propose additional tests through GitHub issues.

## Articles on TDD Katas

1. [Learning Test Driven Development with TDD Katas](http://goo.gl/5NYpVI)
2. [TDD-Kata practices](http://tddkatas.codeplex.com/) - obsolete

## More Flavors

1. [TDD Katas in .NET](https://github.com/garora/TDD-Katas)
2. [TDD Katas in Java](https://github.com/garora/TDD-Katas-Java)
3. [TDD Katas in JavaScript](https://github.com/garora/TDD-Katas-JavaScript)
4. [TDD Katas in Python](https://github.com/garora/TDD-Katas-Python)
5. [TDD Katas in PHP](https://github.com/garora/TDD-Katas-PHP)

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.