import pytest
from reagent_formula import is_valid


@pytest.mark.parametrize('given, expected', [
    ([1, 3, 7], True),
    ([7, 1, 2, 3], False),
    ([1, 3, 5, 7], False),
    ([1, 5, 6, 7, 3], True),
    ([5, 6, 7], True),
    ([5, 6, 7, 8], True),
    ([6, 7, 8], False),
    ([7, 8], True)
])

def test_is_valid(given, expected):
    assert is_valid(given) == expected
