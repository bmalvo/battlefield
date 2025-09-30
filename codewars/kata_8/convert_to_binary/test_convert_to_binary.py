import pytest
from convert_to_binary import to_binary


@pytest.mark.parametrize('given, expected', [
    (1, 1), (2, 10), (3, 11), (5, 101)
])

def test_to_binary(given, expected):
    assert to_binary(given) == expected
