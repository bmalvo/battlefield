import pytest
from how_do_i_compare_numbers import what_is


@pytest.mark.parametrize('given, expected',
                         [(0, 'nothing'),
                          (123, 'nothing'),
                             (-1, 'nothing'),
                             (42, 'everything'),
                             (42 * 42, 'everything squared')])
def test_what_is(given, expected):
    assert what_is(given) == expected
