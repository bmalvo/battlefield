import pytest
from keep_up_the_hoop import hoop_count


@pytest.mark.parametrize('given, expected',[
    (3, "Keep at it until you get it"),
    (11, "Great, now move on to tricks")
])

def test_hoop_count(given, expected):
    assert hoop_count(given) == expected