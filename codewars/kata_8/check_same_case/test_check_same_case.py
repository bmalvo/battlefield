import pytest
from check_same_case import same_case


@pytest.mark.parametrize('given, expected', [(('a', 'g'), 1),
                                             (('A', 'C'), 1),
                                             (('b', 'G'), 0),
                                             (('B', 'g'), 0),
                                             (('0', '?'), -1)])
def test_same_case(given, expected):
    assert same_case(given[0], given[1]) == expected
