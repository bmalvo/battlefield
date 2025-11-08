import pytest
from reverse_list_order import reverse_list



@pytest.mark.parametrize('given, expected', [
    ([1, 2, 3, 4], [4, 3, 2, 1]),
    ([3, 1, 5, 4], [4, 5, 1, 3]),
    ([3, 6, 9, 2], [2, 9, 6, 3]),
    ([1], [1])
])

def test_reverse_list(given, expected):
    assert reverse_list(given) == expected
