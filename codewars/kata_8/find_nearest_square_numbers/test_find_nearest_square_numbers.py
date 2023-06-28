from find_nearest_square_numbers import nearest_sq
import pytest

# test.assert_equals(nearest_sq(1), 1)
#         test.assert_equals(nearest_sq(2), 1)
#         test.assert_equals(nearest_sq(10), 9)
#         test.assert_equals(nearest_sq(111), 121)
#         test.assert_equals(nearest_sq(9999), 10000)


@pytest.mark.parametrize('given, expected', [(1, 1), (2, 1), (10, 9), (111, 121), (9999, 10000)])
def test_nearest_sq(given, expected):
    assert nearest_sq(given) == expected
