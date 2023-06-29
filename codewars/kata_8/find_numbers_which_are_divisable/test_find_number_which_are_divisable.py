from find_number_which_are_divisable import divisible_by
import pytest


@pytest.mark.parametrize('given, expected',
                         [(([1, 2, 3, 4, 5, 6], 2), [2, 4, 6]), (([1, 2, 3, 4, 5, 6], 3), [3, 6]),
                          (([0, 1, 2, 3, 4, 5, 6], 4), [0, 4]), (([0], 4), [0]),
                          (([1, 3, 5], 2), []), (([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1),
                                                 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])])
def test_divisible_by(given, expected):
    assert divisible_by(given[0], given[1]) == expected
