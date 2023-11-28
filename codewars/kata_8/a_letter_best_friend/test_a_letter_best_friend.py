from a_letter_best_friend import best_friend
import pytest


@pytest.mark.parametrize('given, expected', [
    (("he headed to the store", "h", "e"), True),
    (('abcdee', 'e', 'e'), False),
    (("i found an ounce with my hound", "o", "u"),True),
    (("we found your dynamite", "d", "y"), False)])
def test_best_friend(given, expected):
    assert best_friend(given[0], given[1], given[2]) == expected
