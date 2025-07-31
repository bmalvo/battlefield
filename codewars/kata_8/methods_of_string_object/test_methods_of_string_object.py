import pytest
from methods_of_string_object import split_and_merge


@pytest.mark.parametrize('given, expected', [(("My name is John", " "), "M y n a m e i s J o h n"),
                                             (("My name is John", "-"), "M-y n-a-m-e i-s J-o-h-n"),
                                             (("Hello World!", "."), "H.e.l.l.o W.o.r.l.d.!"),
                                             (("Hello World!", ","), "H,e,l,l,o W,o,r,l,d,!")])

def test_split_and_merge(given, expected):
    assert split_and_merge(given[0], given[1]) == expected
