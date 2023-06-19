from double_char import double_char
import pytest


@pytest.mark.parametrize("given, expect",
                         [(("String"), "SSttrriinngg"), (("Hello World"), "HHeelllloo  WWoorrlldd"),
                          (("1234!_ "), "11223344!!__  ")])
def test_double_char(given, expect):
    assert double_char(given) == expect
