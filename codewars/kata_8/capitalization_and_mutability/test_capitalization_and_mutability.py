import pytest
from capitalization_and_mutability import capitalize_word


@pytest.mark.parametrize('given, expected', [

    ('word', 'Word'),
    ('i', 'I'),
    ('glasswear', 'Glasswear')
])

def test_capitalize_word(given, expected):
    assert capitalize_word(given) == expected
