import pytest
from collinearity import collinearity


@pytest.mark.parametrize('given, expected', [((1, 1, 1, 1),True),
                                              ((1, 2, 2, 4),True),
                                              ((1, 1, 6, 1),False),
                                              ((1, 2, -1, -2),True),
                                              ((1, 2, 1, -2),False),
                                              ((4, 0, 11, 0),True),
                                              ((0, 1, 6, 0),False),
                                              ((4, 4, 0, 4),False),
                                              ((0, 0, 0, 0),True),
                                              ((0, 0, 1, 0),True),
                                              ((5, 7, 0, 0),True)])

def test_collinearity(given, expected):
    x1, y1, x2, y2 = given
    assert collinearity(x1, y1, x2, y2) == expected
