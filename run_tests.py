"""Run every kata test suite from the repository root."""

from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parent
SOURCE_DIRECTORY = ROOT / "src"
TEST_PATTERN = "*test*.py"


def discover_kata_tests():
    """Return a combined suite for every kata directory under ``src``."""
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    for kata_directory in sorted(path for path in SOURCE_DIRECTORY.iterdir() if path.is_dir()):
        suite.addTests(
            loader.discover(
                start_dir=str(kata_directory),
                pattern=TEST_PATTERN,
                top_level_dir=str(kata_directory),
            )
        )

    return suite


def main():
    """Run the combined suite and return a shell-compatible status code."""
    result = unittest.TextTestRunner(verbosity=2).run(discover_kata_tests())
    return 0 if result.wasSuccessful() else 1


if __name__ == "__main__":
    raise SystemExit(main())