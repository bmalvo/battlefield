import pytest
from is_it_even import is_even


@pytest.mark.parametrize('given, expected', [
    (0, True),
    (0.5, False),
    (1, False),
    (2, True),
    (-4, True),
    (15, False),
    (20, True),
    (220, True),
    (222222221, False),
    (500000000, True)
])

def test_is_even(given, expected):
    assert is_even(given) == expected