from solve import solve


def test_example_from_statement():
    lines = ["1abc2", "pqr3stu8vwx", "a1b2c3d4e5f", "treb7uchet"]
    assert solve(lines) == 142


def test_single_line():
    assert solve(["a1bc24de"]) == 14


def test_single_digit_counts_twice():
    assert solve(["treb7uchet"]) == 77


def test_only_digits():
    assert solve(["12345"]) == 15


def test_line_without_digits_adds_nothing():
    assert solve(["abc", "1abc2"]) == 12


def test_empty_string():
    assert solve([""]) == 0


def test_empty_list():
    assert solve([]) == 0
