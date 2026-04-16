import pytest
from reversing_words_in_a_string import reverse


@pytest.mark.parametrize('given, expected', [
    ('Hello World', 'World Hello'),
   ('Hi There.', 'There. Hi')
])

def test_reverse(given, expected):
    assert reverse(given) == expected
