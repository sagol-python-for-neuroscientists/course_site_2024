""" Tests for question 1 - Morse code translator """
from pathlib import Path

OUTPUT_FILE_NAME = "lorem_morse.txt"
OUTPUT_PATH = Path(__file__).parent / OUTPUT_FILE_NAME


def test_file_exists():
    assert OUTPUT_PATH.exists()


def test_file_valid():
    data = Path(OUTPUT_FILE_NAME).read_text()
    assert data.count("-") == 2748
    assert data.count(".") == 4175
    assert data.count("\n") == 453


def test_individual_lines():
    with open(OUTPUT_FILE_NAME) as f:
        data = f.readlines()
    assert len(data) == 454
    assert data[-1] == ".-....--.-.-..-....-.-.-"
    assert data[3].startswith(".....-")


if __name__ == "__main__":
    methods = ["test_file_exists", "test_file_valid", "test_individual_lines"]
    errors = []

    for method in methods:
        try:
            eval(method)()
        except AssertionError as e:
            errors.append(f"Failed when testing method 'test_{method}': {e}")
            break

    if errors:
        raise AssertionError(errors)
    else:
        print("Tests pass successfully.")
