import pytest
from permutation import all_permutations


@pytest.mark.parametrize('given, expected', [('ab', ['ab','ba']),
                   ('aabb', ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa'])])
def test_solution(given, expected):
    assert all_permutations(given) == expected
