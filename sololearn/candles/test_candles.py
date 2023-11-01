from candles import candles_to_order
import pytest


@pytest.mark.parametrize('given, expected',[(0, 9),(1, 18)])
def test_canles_to_order(given, expected):
    assert candles_to_order(given) == expected
