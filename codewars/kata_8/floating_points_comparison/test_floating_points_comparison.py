from floating_points_comparison import approx_equals
import pytest


@pytest.mark.parametrize('given, expected', [((175.9827, 82.25), False),
                                             ((-156.24037, -156.24038), True),
                                             ((123.2345, 123.234501), True),
                                             ((1456.3652, 1456.3641), False),
                                             ((-1.234, -1.233999), True),
                                             ((98.7655, 98.7654999), True),
                                             ((-7.28495, -7.28596), False)])
def test_approx_equals(given, expected):
    assert approx_equals(given[0], given[1]) == expected
