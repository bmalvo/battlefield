import pytest
from messi_goals_function import goals


@pytest.mark.parametrize('given, expected', [
    ((0, 0, 0), 0),
    ((5, 10, 2), 17)
])

def test_goals(given, expected):
    laLiga, copaDelRey, championsLeague = given
    assert goals(laLiga, copaDelRey, championsLeague) == expected
