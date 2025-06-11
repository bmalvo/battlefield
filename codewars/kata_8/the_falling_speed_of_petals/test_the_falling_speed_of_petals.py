import pytest
from the_falling_speed_of_petals import sakura_fall


@pytest.mark.parametrize('given, expected',
                         [ (5, 80),
                          (10, 40),
                             (-1, 0),
                             (0, 0)
                             ])
def test_sakura_fall(given, expected):
    assert sakura_fall(given) == expected
