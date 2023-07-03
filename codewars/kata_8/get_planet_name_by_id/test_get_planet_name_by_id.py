from get_planet_name_by_id import get_planet_name
import pytest


@pytest.mark.parametrize('given, expected',
                         [(2, 'Venus'), (5, 'Jupiter'), (3, 'Earth'), (4, 'Mars'), (8, 'Neptune'),
                          (1, 'Mercury')])
def test_get_planet_name(given, expected):
    assert get_planet_name(given) == expected
