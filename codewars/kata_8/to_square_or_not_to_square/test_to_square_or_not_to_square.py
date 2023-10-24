from to_square_or_not_to_square import square_or_square_root
import pytest



@pytest.mark.parametrize('given, expected', 
                         [([4, 3, 9, 7, 2, 1 ], [2, 9, 3, 49, 4, 1]),
                          ([100, 101, 5, 5, 1, 1], [10, 10201, 25, 25, 1, 1]),
                          ([1, 2, 3, 4, 5, 6], [1, 4, 9, 2, 25, 36])])
def test_square_or_square_root(given, expected):
    assert square_or_square_root(given) == expected 
    