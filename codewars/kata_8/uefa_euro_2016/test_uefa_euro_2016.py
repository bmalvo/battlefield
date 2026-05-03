import pytest
from uefa_euro_2016 import uefa_euro_2016


@pytest.mark.parametrize('given, expected', [
    ((['Germany', 'Ukraine'], [2, 0]), 
     "At match Germany - Ukraine, Germany won!"),
    ((['Belgium', 'Italy'],[0, 2]), 
     "At match Belgium - Italy, Italy won!"),
    ((['Portugal', 'Iceland'], [1, 1]), 
     "At match Portugal - Iceland, teams played draw."),
    ((['Albania', 'Switzerland'], [1, 2]), 
     "At match Albania - Switzerland, Switzerland won!"),
    ((['Republic of Ireland', 'Sweden'], [0, 0]), 
     "At match Republic of Ireland - Sweden, teams played draw.")
])


def test_uefa_euro_2016(given, expected):
    teams, scores = given[0], given[1]
    assert uefa_euro_2016(teams, scores) == expected
