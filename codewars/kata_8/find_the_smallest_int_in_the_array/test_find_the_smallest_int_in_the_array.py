from find_the_smallest_int_in_the_array import find_smallest_int
import pytest

@pytest.mark.parametrize('given, expected',[([34, 15, 88, 2], 2),
                                            ([34, -345, -1, 100], -345),
                                            ([1,1,1,1,1], 1)])
def test_find_smallest_int(given, expected):
    assert find_smallest_int(given) == expected
