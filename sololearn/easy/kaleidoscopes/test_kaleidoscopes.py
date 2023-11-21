from kaleidoscopes import total_cost
import pytest


@pytest.mark.parametrize('given, expected',[(1, 5.35),(3, 14.45),(2, 9.63)])
def test_total_cost(given, expected):
    assert total_cost(given) == expected
