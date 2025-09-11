import pytest
from reversed_strings import solution


@pytest.mark.parametrize('given, expected', [
    (('world'), 'dlrow'),
    (('hello'), 'olleh'),
    ((''), ''),
    (('h'), 'h')
])

def test_solution(given, expected):
    assert solution(given) == expected
