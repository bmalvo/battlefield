from reversed_words import reverse_words
import pytest


@pytest.mark.parametrize('given, expected', [
    ("The greatest victory is that which requires no battle", 
     "battle no requires which that is victory greatest The"),
     ('Hello World!', "World! Hello")])
def test_reverse_words(given, expected):
    assert reverse_words(given) == expected
