import pytest
from thinkful_logic_drills_traffic_light import update_light


@pytest.mark.parametrize('given, expected', [(('green'), 'yellow'),
                                             (('yellow'), 'red'),
                                             (('red'), 'green')])

def test_update_light(given, expected):
    assert update_light(given) == expected
