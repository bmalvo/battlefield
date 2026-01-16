import pytest
from sum_of_differences_in_array import sum_of_differences


@pytest.mark.parametrize('given, expected', [
    ([1, 2, 10], 9),
    ([-3, -2, -1], 2),
    ([1, 1, 1, 1, 1], 0),
    ([-17, 17], 34),
    ([], 0),
    ([0], 0),
    ([-1], 0),
    ([1], 0),
])
def test_sum_of_differences(given, expected):
    assert sum_of_differences(given) == expected
