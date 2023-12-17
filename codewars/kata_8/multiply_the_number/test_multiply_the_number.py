import pytest
from multiply_the_number import multiply


@pytest.mark.parametrize('given, expected', [(3, 15), (10, 250),
                                             (200, 25000), (0, 0),
                                             (-3, -15)])
def test_multiply(given, expected):
    assert multiply(given) == expected
