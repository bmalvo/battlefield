from vowel_counter import vowel_counter
import pytest


@pytest.mark.parametrize('given, expected', [('this is a sentence', 6),
                                             ('Th3re @rent any', 3),
                                             ('Is there life on Mars?', 7)])
def test_vowel_counter(given, expected):
    assert vowel_counter(given) == expected
