import pytest
from pillars import pillars


@pytest.mark.parametrize('given, expected', [
    ((2, 20, 25), 2000),
    ((1, 10, 10), 0),
    ((11, 15, 30), 15270)
])
def test_pillars(given, expected):
    num_pill, dist, width = given[0], given[1], given[2]
    assert pillars(num_pill, dist, width) == expected
