import pytest
from stringy_strings import stringy


@pytest.mark.parametrize('given, expected', [
    (3, '101'),
    (5, '10101'),
    (12, '101010101010'),
    (26, '10101010101010101010101010'),
    (28, '1010101010101010101010101010')
])

def test_stringy(given, expected):
    assert stringy(given) == expected