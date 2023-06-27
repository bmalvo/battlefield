from find_multiples_of_a_number import find_multiples
import pytest


@pytest.mark.parametrize('given, expected', [((5, 25), [5, 10, 15, 20, 25]), ((1, 2), [1, 2])])
def test_find_multiples(given, expected):
    assert find_multiples(given[0], given[1]) == expected
