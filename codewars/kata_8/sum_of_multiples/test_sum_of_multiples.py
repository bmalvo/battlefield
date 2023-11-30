import pytest
from sum_of_multiples import sum_mul


@pytest.mark.parametrize('given, expected', [((2, 9), 20), ((3,13), 30),
                                             ((4, 123), 1860), ((2, 2), 0),
                                             ((4, -7), 'INVALID')])
def test_sum_mul(given, expected):
    assert sum_mul(given[0], given[1]) == expected
