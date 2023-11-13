from multiples import calc_multiples
import pytest


@pytest.mark.parametrize('given, expected', [(10, 23),(100, 2318),
                                             (4242, 4198308)])
def test_calc_multiples(given, expected):
    assert calc_multiples(given) == expected
