from land_ho import time_to_get_shore
import pytest


@pytest.mark.parametrize('given, expected', [(15, 10),(1, 10),
                                             (80, 90)])
def test_time_to_get_shore(given, expected):
    assert time_to_get_shore(given) == expected
