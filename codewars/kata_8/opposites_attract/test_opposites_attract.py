import pytest
from opposites_attract import lovefunc


@pytest.mark.parametrize('given, expected', [
    ((1, 4), True),
    ((2, 2), False),
    ((0, 1), True),
    ((0, 0), False)
])

def test_lovefunc(given, expected):
    flower1, flower2 = given
    assert lovefunc(flower1, flower2) == expected 
