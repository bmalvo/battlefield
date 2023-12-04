from school_paperwork import paperwork
import pytest


@pytest.mark.parametrize('given, expected', [((5, 5), 25), ((-5, 5), 0), 
                                             ((5, -5), 0), ((5, 0), 0)])
def test_paperwork(given, expected):
    assert paperwork(given[0], given[1]) == expected
