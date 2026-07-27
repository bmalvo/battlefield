import pytest
from cmyk_to_rgb import color_translator


@pytest.mark.parametrize('given, expected',[
    ((0.4, 0.49, 0.552, 0.36), (98, 83, 73))
])

def test_color_translator(given, expected):
    c, m, y, k = given
    r, g, b = expected
    assert color_translator(c, m, y, k) == f'{r}, {g}, {b}'
