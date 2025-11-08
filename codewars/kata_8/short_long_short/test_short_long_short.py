import pytest
from short_long_short import solution


@pytest.mark.parametrize('given, expected',[
    (('45', '1'), '1451'),
    (('13', '200'), '1320013'),
    (('Soon', 'Me'), 'MeSoonMe'),
    (('U', 'False'), 'UFalseU')
])

def test_solution(given, expected):
    a, b = given
    assert solution(a, b) == expected