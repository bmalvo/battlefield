from average_word_length import average_all_words
import pytest


@pytest.mark.parametrize('given, expected', [
                        ('this phrase has multiple words', 6),
                        ('Can you not do that?', 3),
                        ('The longest word in the dictionary is...', 5)])
def test_average_all_words(given, expected):
    assert average_all_words(given) == expected
