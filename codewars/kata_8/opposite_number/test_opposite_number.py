import pytest
from opposite_number import opposite


@pytest.mark.parametrize('given, expected', [
    (1, -1),
    (25.6, -25.6),
    (0, 0),
    (1425.2222, -1425.2222),
    (-3.1458, 3.1458),
    (-95858588225, 95858588225)
])

def test_opposite(given, expected):
    assert opposite(given) == expected
