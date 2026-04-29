import pytest
from validate_code_with_simple_regex import validate_code


@pytest.mark.parametrize('given, expected', [
    (123, True),
    (248, True),
    (8, False),
    (321, True),
    (9453, False)
])

def test_validate_code(given, expected):
    assert validate_code(given) == expected
 