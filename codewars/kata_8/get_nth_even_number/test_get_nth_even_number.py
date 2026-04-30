import pytest
from get_nth_even_number import nth_even


@pytest.mark.parametrize('given, expected',[
    (1, 0),
    (2, 2),
    (3, 4),
    (100, 198),
    (1298734, 2597466)
])

def test_nth_even(given, expected):
    assert nth_even(given) == expected
