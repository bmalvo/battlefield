from is_the_string_uppercase import is_uppercase
import pytest


@pytest.mark.parametrize('given, expected',
                         [("c", False), ("C", True), ("hello I AM DONALD", False),
                          ("HELLO I AM DONALD", True), ("$%&", True),
                          ("ACSKLDFJSgSKLDFJSKLDFJ", False)])
def test_is_upper(given, expected):
    assert is_uppercase(given) == expected
