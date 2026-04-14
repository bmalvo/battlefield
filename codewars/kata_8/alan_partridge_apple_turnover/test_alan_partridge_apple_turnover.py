import pytest
from alan_partridge_apple_turnover import apple


@pytest.mark.parametrize('given, expected', [
    ('50', "It's hotter than the sun!!"),
    (4, "Help yourself to a honeycomb Yorkie for the glovebox."),
    ("12", "Help yourself to a honeycomb Yorkie for the glovebox."),
    (60, "It's hotter than the sun!!")
])

def test_apple(given, expected):
    assert apple(given) == expected
