import pytest
from what_is_the_real_floor import get_real_floor


@pytest.mark.parametrize('given, expected', [
    (1, 0),
    (5, 4),
    (15, 13),
    (-3, -3),
    (0, 0)
])

def test_get_real_flor(given, expected):
    assert get_real_floor(given) == expected
