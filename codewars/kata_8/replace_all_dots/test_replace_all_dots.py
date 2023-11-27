from replace_all_dots import replace_dots
import pytest


@pytest.mark.parametrize('given, expected', [
                                     ('test.for.code', 'test-for-code'),
                                     ('test.number.two', 'test-number-two')])
def test_replace_dots(given, expected):
    assert replace_dots(given) == expected
