from aspect_ratio_cropping_1 import aspect_ratio
import pytest


@pytest.mark.parametrize('given, expected',[((640, 480,), (854, 480)),
                                            ((960, 720), (1280, 720)),
                                            ((1440, 1080), (1920, 1080)),
                                            ((1920, 1440), (2560, 1440))])
def test_aspect_ratio(given, expected):
    assert aspect_ratio(given[0], given[1]) == expected
