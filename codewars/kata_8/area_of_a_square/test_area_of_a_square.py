import pytest
from area_of_a_square import square_area

@pytest.mark.parametrize('given, expected', [(2, 1.62),
                                             (0, 0),
                                             (14.05, 80),
                                             (1, 0.41), 
                                             (100, 4052.85)])
def test_square_area(given, expected):
    assert square_area(given) == expected