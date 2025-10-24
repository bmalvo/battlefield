import pytest
from triple_trouble import triple_trouble


@pytest.mark.parametrize('given, expected', [
    (("aaa", "bbb", "ccc"), "abcabcabc"),
    (("aaaaaa", "bbbbbb", "cccccc"), "abcabcabcabcabcabc"),
    (("burn", "reds", "roll"), "brrueordlnsl"),
    (("Bm", "aa", "tn"), "Batman"),
    (("LLh", "euo", "xtr"), "LexLuthor")
])

def test_triple_trouble(given, expected):
    one, two, three = given
    assert triple_trouble(one, two, three) == expected