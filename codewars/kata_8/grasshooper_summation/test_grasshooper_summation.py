import pytest
from grasshooper_summation import summation


@pytest.mark.parametrize('given, expected', [(2, 3), (8, 36)])
def test_summation(given, expected):
    assert summation(given) == expected
