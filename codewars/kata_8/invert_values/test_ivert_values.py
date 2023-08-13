import pytest
from invert_values import invert

@pytest.mark.parametrize('given, expected', 
                         [([1, -2, 3, -4, 5], [-1, 2, -3, 4, -5]),
                          ([1, 2, 3, 4], [-1, -2, -3, -4]),
                          ([], [])])
def test_invert(given, expected):
    assert invert(given) == expected
