import pytest
from vexing_vanishing_values import mul_by_n


@pytest.mark.parametrize('given, expected', 
                         [(([1, 2, 3], 4), [4, 8, 12]),
                         (([9, 1], 9), [81, 9]),
                         (([5, 5, 5, 5, 5], 1), [5, 5, 5, 5, 5]),
                          (([5, 5, 5, 5, 5], 2), [10, 10, 10, 10, 10]),
                          (([77, 88], 0), [0, 0])])
def test_mul_by_n(given, expected):
    assert mul_by_n(given[0], given[1]) == expected
