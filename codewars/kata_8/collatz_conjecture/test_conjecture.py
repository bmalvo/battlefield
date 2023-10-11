from collatz_conjecture import hotpo
import pytest

@pytest.mark.parametrize('given, expected', [(5, 5),(1, 0),(6, 8), (23, 15)])
def test_hotpo(given, expected):
    assert hotpo(given) == expected
