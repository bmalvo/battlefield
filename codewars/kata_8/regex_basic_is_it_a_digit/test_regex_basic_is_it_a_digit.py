import pytest
from regex_basic_is_it_a_digit import is_digit


@pytest.mark.parametrize('given, expected', [('0', True), ('6', True), 
                                             ('d3', False), ('21', False)])
def test_is_digit(given, expected):
    assert is_digit(given) == expected
