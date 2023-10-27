from sum_of_positive import positive_sum
import pytest


@pytest.mark.parametrize('given, expected', [([1,2,3,4,5],15), 
                                             ([1,-2,3,4,5],13),
                                             ([-1,2,3,4,-5],9)])
def test_positive_sum(given, expected):
    assert positive_sum(given) == expected
