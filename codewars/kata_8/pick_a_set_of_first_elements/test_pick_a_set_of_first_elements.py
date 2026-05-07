import pytest
from pick_a_set_of_first_elements import first

seq = ['a', 'b', 'c', 'd', 'e']

@pytest.mark.parametrize('given, expected', [
    ((seq, None), ['a']),
    ((seq, 0), []),
    ((seq, 1), ['a']),
    ((seq, 2), ['a', 'b']),
    ((seq, 10), ['a', 'b', 'c', 'd', 'e'])
])

def test_first(given, expected):
    assert first(given[0], given[1]) == expected
