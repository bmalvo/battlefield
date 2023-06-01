import pytest
from convert_a_string_to_a_number import string_to_number


@pytest.mark.parametrize('given, expect', [('1234', 1234), ('-3', -3), ('69', 69)])
def test_string_to_number(given, expect):
    assert string_to_number(given) == expect
