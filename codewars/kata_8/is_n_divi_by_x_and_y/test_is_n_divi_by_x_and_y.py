from is_n_divi_by_x_and_y import is_divisible
import pytest


@pytest.mark.parametrize('given, expected',
                         [((3, 2, 2), False), ((3, 3, 4), False), ((12, 3, 4), True)])
def test_is_divisible(given, expected):
    assert is_divisible(given[0], given[1], given[2]) == expected
