import pytest
from get_character_from_ascii_value import get_char


@pytest.mark.parametrize('given, expected', [

        (65,'A'),
        (33,'!'),
        (34,'"'),
        (35,'#'),
        (36,'$'),
        (37,'%'),
        (38,'&')
])

def test_get_char(given, expected):
    assert get_char(given) == expected
