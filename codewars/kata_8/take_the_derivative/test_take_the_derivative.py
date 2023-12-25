import pytest

from take_the_derivative import derive


@pytest.mark.parametrize('give, expect', [((7, 8), "56x^7"), ((5, 9), "45x^8"), 
                                          ((6, 2), '12x^2')])
def test_derive(give, expect):
    assert derive(give[0], give[1]) == expect
