import pytest
from halloween_candy import chance_on_bill

@pytest.mark.parametrize('given, expected', [(4, 50), (3, 67), (5, 40), 
                                             (100, 2)])
def test_chance(given, expected):
    assert chance_on_bill(given) == expected
