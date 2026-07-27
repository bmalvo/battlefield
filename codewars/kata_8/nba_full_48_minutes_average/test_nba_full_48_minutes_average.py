import pytest
from nba_full_48_minutes_average import nba_extrap


@pytest.mark.parametrize('given, expected', [
    ((12, 20), 28.8),
    ((10, 10), 48.0),
    ((5, 17), 14.1),
    ((0, 0), 0),
    ((30.8, 34.7), 42.6),
    ((22.9, 33.8), 32.5)
])

def test_nba_extrap(given, expected):
    ppg, mpg = given[0], given[1]
    assert nba_extrap(ppg, mpg) == expected
