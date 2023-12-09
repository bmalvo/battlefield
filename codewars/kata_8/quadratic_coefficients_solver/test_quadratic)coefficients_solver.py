import pytest
from quadratic_coefficients_solver import quadratic


@pytest.mark.parametrize('given, expected', [((0, 1), (1, -1, 0)),
                                             ((4, 9), (1, -13, 36)),
                                             ((2, 6), (1, -8, 12)),
                                             ((-5, -4), (1, 9, 20))])
def test_quadratic(given, expected):
    assert quadratic(given[0], given[1]) == expected
