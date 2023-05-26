from bin_to_decimal import bin_to_decimal
import pytest


@pytest.mark.parametrize('given, expected', [(("0"), 0), (("10"), 2), (("11"), 3), (("101010"), 42), (("1001001"), 73)])
def test_bin_to_decimal(given, expected):
    assert bin_to_decimal(given) == expected
