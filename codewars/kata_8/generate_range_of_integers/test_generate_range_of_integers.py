import pytest
from generate_range_of_integers import generate_range


@pytest.mark.parametrize('start, stop, step, expected',[
                 (1, 10, 1,  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),
                 (-10, 1, 1, [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1]),
                 (1, 15, 20, [1])])
def test_generate_range(start, stop, step, expected):
    assert generate_range(start, stop, step) == expected
