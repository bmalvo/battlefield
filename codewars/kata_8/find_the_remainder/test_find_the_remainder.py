import pytest
from find_the_remainder import remainder


@pytest.mark.parametrize('given, expected', [((17, 5),2), ((13, 72), 7), 
                                             ((0, -1), 0), ((0, 1), None)])
def test_remainder(given, expected):
    assert remainder(given[0], given[1]) == expected
