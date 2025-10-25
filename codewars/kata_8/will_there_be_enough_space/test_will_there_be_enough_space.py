import pytest
from will_there_be_enough_space import enough


@pytest.mark.parametrize('given, expected', [
    ((10, 5, 5), 0),
    ((100, 60, 50), 10),
    ((20, 5, 5), 0)
])

def test_enough(given, expected):
    cap, on, wait = given
    assert enough(cap, on, wait) == expected