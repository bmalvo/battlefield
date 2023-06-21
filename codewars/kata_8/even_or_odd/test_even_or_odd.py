from even_or_odd import even_or_odd
import pytest


@pytest.mark.parametrize('given, expected', [(2, 'Even'), (4, 'Even'), (6, 'Even'), (8, 'Even')])
def test_return_even_or_odd_is_even(given, expected):
    assert even_or_odd(given) == expected


@pytest.mark.parametrize('given, expected', [(1, 'Odd'), (3, 'Odd'), (5, 'Odd'), (7, 'Odd')])
def test_return_even_or_odd_is_odd(given, expected):
    assert even_or_odd(given) == expected
