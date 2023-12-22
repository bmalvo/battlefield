import pytest
from usd_to_cny import usdcny


@pytest.mark.parametrize('given, expected', [(15, "101.25 Chinese Yuan"),
                                             (465, "3138.75 Chinese Yuan")])
def test_usdcny(given, expected):
    assert usdcny(given) == expected
