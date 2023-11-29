from is_it_a_number import is_digit
import pytest


@pytest.mark.parametrize('given, expected', [('3', True), (' 3 ', True),
                                             ('-3.23', True), ('3-4', False),
                                             (' 3  5', False), ('zero', False)])
def test_is_digit(given, expected):
    assert is_digit(given) == expected
