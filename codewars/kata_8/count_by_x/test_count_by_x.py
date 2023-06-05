from count_by_x import count_by
import pytest


@pytest.mark.parametrize('given, excepted',
                         [((1, 10), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), ((2, 5), [2, 4, 6, 8, 10])])
def test_count_by_x(given, excepted):
    print(given)
    print(excepted)
    assert count_by(given[0], given[1]) == excepted
