# TDD Katas - Python

## Description

A collection of Python Test-Driven Development (TDD) katas. Each kata is kept in its own directory under `src` with a standard-library `unittest` suite so it can be practiced independently.

## Requirements

- Python 3.11 or newer (use a currently maintained Python 3 release).
- No third-party Python packages, Node.js, or npm packages are required. The project and tests use only Python's standard library; do not run `pip install`.
- A terminal/command prompt is needed to run the test runner.
- Git is optional: clone the repository with Git, or download the source archive from GitHub.

### Install Python

Python is an interpreter, so a machine without a compatible Python installation must install one before it can run this project. Choose an official or operating-system-supported Python 3.11+ distribution:

- **Windows:** follow the [official Windows installation guide](https://docs.python.org/3/using/windows.html) or download Python from [python.org](https://www.python.org/downloads/). After installation, open a new terminal and verify `python --version`. If the Python launcher is installed and configured, `py -3 --version` is another option.
- **macOS:** follow the [official macOS guide](https://docs.python.org/3/using/mac.html) and use a supported installer from [python.org](https://www.python.org/downloads/macos/). Verify `python3 --version`. Do not replace or remove the Apple-controlled system Python.
- **Linux and other Unix-like systems:** install Python 3.11+ through your distribution's supported package manager or follow the [official Unix installation guide](https://docs.python.org/3/using/unix.html). Verify `python3 --version`.
- **Other operating systems/devices:** this repository is pure Python, but it is not a standalone executable and cannot run on every device automatically. The OS must have a compatible Python 3.11+ interpreter and a command-line environment; installation and compatibility on other platforms are not guaranteed by this project.

Once the repository files and Python are installed, running the tests does not require network access or downloading additional packages.
## Run the Tests

From the repository root, run every implemented kata test suite:

```powershell
# Windows PowerShell / Command Prompt
python run_tests.py
# Or, if the Python launcher is installed and configured:
py -3 run_tests.py
```

```sh
# macOS / Linux / Unix-like shells
python3 run_tests.py
```

Use whichever command refers to the installed Python 3.11+ interpreter. The runner discovers tests in every kata directory, including directories whose names contain spaces, and returns a non-zero exit code if any test fails. No `pip`, npm, or other package installation is needed.

To run an individual suite, for example:

```powershell
python -m unittest discover -s "src/FizzBuzz" -p "test_fizz_buzz.py" -v
```

```sh
python3 -m unittest discover -s "src/FizzBuzz" -p "test_fizz_buzz.py" -v
```
## Implemented Katas

- [Recently Used List](src/Recently%20Used%20List/)
- [String Sum](src/String%20Sum/)
- [String Calculator](src/String%20Calculator/)
- [Bowling Game](src/Bowling%20Game/)
- [Calc Stats](src/Calc%20Stats/)
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