import pytest
from enumerable_magic_does_my_list_include_this import include


lst = [0, 1, 2, 3, 5, 8, 13, 2, 2, 2, 11]

@pytest.mark.parametrize('given, expected', [
    ((lst, 100), False),
    ((lst, 2), True),
    ((lst, 11), True),
    ((lst, "2"), False),
    ((lst, 0), True),
    (([], 0), False)
])

def test_include(given, expected):
    arr, item = given[0], given[1]
    assert include(arr, item) == expected
