from highest_and_lowest import high_and_low
import pytest


@pytest.mark.parametrize('given, expected', [('1 2 3 4 5', '5 1'),
                                             ('1 2 -3 4 5', '5 -3'),
                                             ('1 9 3 4 -5', '9 -5'),
                                             ('99 3 54 0', '99 0')])
def test_high_and_low2(given, expected):
    assert high_and_low(given) == expected
