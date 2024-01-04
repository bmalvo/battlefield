from twice_as_old import twice_as_old
import pytest


@pytest.mark.parametrize('given, expected',
                         [((36, 7), 22), ((55, 30), 5), ((42, 21), 0), 
                          ((22, 1), 20), ((29, 0), 29)])
def test_twice_as_old(given, expected):
    assert twice_as_old(given[0], given[1]) == expected
