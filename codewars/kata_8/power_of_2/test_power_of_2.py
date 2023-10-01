from power_of_2 import powers_of_two
import pytest


@pytest.mark.parametrize('given, expected', [(0, [1]), (1, [1, 2]), 
                                             (4, [1, 2, 4, 8, 16])])
def test_powers_of_2(given, expected):
    assert powers_of_two(given) == expected
