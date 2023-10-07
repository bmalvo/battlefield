from reduce_but_grow import grow
import pytest


@pytest.mark.parametrize('given, expected',
                         [([1, 2, 3], 6), ([4, 1, 1, 1, 4], 16), 
                          ([2, 2, 2, 2, 2, 2], 64)])
def test_reduce_but_grow(given, expected):
    assert grow(given) == expected
