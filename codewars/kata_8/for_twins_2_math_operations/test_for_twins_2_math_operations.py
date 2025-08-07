import pytest
from for_twins_2_math_operations import ice_brick_volume


@pytest.mark.parametrize('given, expected', [((1, 10, 2), 16),
                                             ((5, 30, 7), 1150)])

def test_ice_brick_volume(given, expected):
    assert ice_brick_volume(given[0], given[1], given[2]) == expected
