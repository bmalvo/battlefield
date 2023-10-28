from differenc_of_volumes_of_cuboids import find_difference
import pytest


@pytest.mark.parametrize('given, expected', [(([3, 2, 5], [1, 4, 4]), 14,),
                                             (([9, 7, 2], [5, 2, 2]), 106)])
def test_find_difference(given, expected):
    assert find_difference(given[0], given[1]) == expected
