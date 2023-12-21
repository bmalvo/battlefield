import pytest
from simple_validation_of_a_username_with_regex import validate_usr


@pytest.mark.parametrize('given, expected', [
                ('asddsa', True), ('a', False), ('Hass', False),
                ('Hasd_12assssssasasasasasaasasasasas', False), ('', False),
                ('____', True), ('012', False), ('p1pp1', True), 
                ('asd43 34', False), ('asd43_34', True),
                ('too_long_username_with_only_valid_characters_123', False)])
def test_validate_usr(given, expected):
    assert validate_usr(given) == expected
