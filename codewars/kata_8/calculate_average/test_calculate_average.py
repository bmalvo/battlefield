from calculate_average import find_average
import pytest


@pytest.mark.parametrize('given, expected', [([1, 2, 3], 2), ([], 0),
                                             ([1, 2], 1.5)])
def test_find_average(given, expected):
    assert find_average(given) == expected
