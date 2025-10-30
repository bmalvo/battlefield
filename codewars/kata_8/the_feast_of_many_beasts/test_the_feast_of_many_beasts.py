import pytest
from the_feast_of_many_beasts import feast


@pytest.mark.parametrize('given, expected', [
    (("great blue heron", "garlic naan"), True),
    (("chickadee", "chocolate cake"), True),
    (("brown bear", "bear claw"), False),
])

def test_feast(given, expected):
    beast, dish = given
    assert feast(beast, dish) == expected