import pytest
from jumping_dutch_act import sc


@pytest.mark.parametrize('given, expected', [
    ((1), ""),
    ((-1), ""),
    ((2), "Aa~ Pa! Aa!"),
    ((6), "Aa~ Aa~ Aa~ Aa~ Aa~ Pa! Aa!"),
    ((7), "Aa~ Aa~ Aa~ Aa~ Aa~ Aa~ Pa!"),
    ((10), "Aa~ Aa~ Aa~ Aa~ Aa~ Aa~ Aa~ Aa~ Aa~ Pa!")
])

def test_sc(given, expected):
    assert sc(given) == expected
