from contamination import contamination
import pytest


@pytest.mark.parametrize('given, expected',
                         [(("abc", "z"), "zzz"), (("", "z"), ""), (("abc", ""), ""),
                          (("_3ebzgh4", "&"), "&&&&&&&&"), (("//case", " "), "      ")])
def test_contamination(given, expected):
    assert contamination(given[0], given[1]) == expected
