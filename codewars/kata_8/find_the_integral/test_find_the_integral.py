import pytest
from find_the_integral import integrate


@pytest.mark.parametrize('given, expected', [((3, 2),"1x^3"),
                                             ((12, 5), "2x^6"),
                                             ((20, 1), "10x^2"),
                                             ((40, 3), "10x^4"),
                                             ((90, 2),  "30x^3")])
def test_integrate(given, expected):
    assert integrate(given[0], given[1]) == expected
