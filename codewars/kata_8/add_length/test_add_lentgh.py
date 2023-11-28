from add_length import add_length
import pytest


@pytest.mark.parametrize('given, expected', [
                            ("apple ban", ["apple 5", "ban 3"]),
                            ("you will win", ["you 3", "will 4", "win 3"])])
def test_add_length(given, expected):
    assert add_length(given) == expected
