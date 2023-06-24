from filling_an_array import arr
import pytest


@pytest.mark.parametrize('given, expected', [(4, [0, 1, 2, 3]), (0, [])])
def test_arr(given, expected):
    assert arr(given) == expected
