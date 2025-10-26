import pytest
from i_love_you_a_little_a_lot_passionately_not_at_all import how_much_i_love_you


@pytest.mark.parametrize('given, expected', [
    ((7), "I love you"),
    ((3), "a lot"),
    ((6), "not at all")
])

def test_how_much_i_love_you(given, expected):
    assert how_much_i_love_you(given) == expected