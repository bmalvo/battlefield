import pytest
from circles_in_polygon import circle_diameter


@pytest.mark.parametrize('side, side_length, expected', [(4, 5, 5.000),
                                                        (8, 9, 21.728),
                                                        (3 , 4, 2.309)])
def test_circle_diameter(side, side_length, expected):
    assert circle_diameter(side, side_length) == expected
