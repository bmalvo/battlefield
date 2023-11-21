from hovercraft import profitable_hovercraft
import pytest


@pytest.mark.parametrize('given, expected', [(5, 'Loss'),(7, 'Broke Even'),
                                             (10, 'Profit')])
def test_profitable_hovercreft(given, expected):
    assert profitable_hovercraft(given) == expected
