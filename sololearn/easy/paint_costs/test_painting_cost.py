from paint_costs import painting_cost
import pytest


@pytest.mark.parametrize('given, expected', [(10, 99), (2, 55), (20, 154)])
def test_painting_cost(given, expected):
    assert painting_cost(given) == expected
