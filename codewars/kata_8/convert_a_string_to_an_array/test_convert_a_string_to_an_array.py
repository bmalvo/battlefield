from convert_a_string_to_an_array import string_to_array
import pytest


@pytest.mark.parametrize('given, expected',
                         [(("Robin Singh"), ["Robin", "Singh"]), (("CodeWars"), ["CodeWars"]), (
                         ("I love arrays they are my favorite"),
                         ["I", "love", "arrays", "they", "are", "my", "favorite"]),
                          (("1 2 3"), ["1", "2", "3"]), ((""), [""])])
def test_string_to_array(given, expected):
    assert string_to_array(given) == expected
