from is_he_gonna_survive import hero
import pytest


@pytest.mark.parametrize('given, expected', [((10, 5), True),((7, 4), False),
                                             ((4, 5), False),((100, 40), True),
                                             ((1500, 751), False),
                                             ((0, 1), False)])
def test_hero(given, expected):
    assert hero(given[0], given[1]) == expected
