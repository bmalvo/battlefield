from multiple_of_three_or_five import solution
import pytest


@pytest.mark.parametrize('given, expected', [(10, 23), (4, 3), (16, 60), (-14, 0)])
def test_solution(given, expected):
    assert solution(given) == expected
