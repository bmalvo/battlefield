from isogram_detector import isogram_detector
import pytest


@pytest.mark.parametrize('given, expected', [('turbulence', False),
                                             ('come', True),
                                             ('cerebral', False)])
def test_isogram_detector(given, expected):
    print(expected)
    assert isogram_detector(given) == expected
