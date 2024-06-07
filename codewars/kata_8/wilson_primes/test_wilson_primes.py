from wilson_primes import am_i_wilson
import pytest


@pytest.mark.parametrize('given, expected', [(0, False), (3, False), 
                                             (5, True), (13, True)])
def test_am_i_wilson(given, expected):
    assert am_i_wilson(given) == expected
