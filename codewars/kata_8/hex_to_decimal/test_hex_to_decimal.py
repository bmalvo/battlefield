from hex_to_decimal import hex_to_dec
import pytest


@pytest.mark.parametrize('given, expected', [("1", 1), ("a", 10), ("10", 16)])
def test_hex_to_dec(given, expected):
    assert hex_to_dec(given) == expected
