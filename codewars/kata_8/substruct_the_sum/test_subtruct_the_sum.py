from subtruct_the_sum import subtract_sum
import pytest


@pytest.mark.parametrize('given, expected', [(10, 'apple')])
def test_subtruct_sum(given, expected):
    assert subtract_sum(given) == expected
