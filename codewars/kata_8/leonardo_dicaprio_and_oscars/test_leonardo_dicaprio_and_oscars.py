import pytest
from leonardo_dicaprio_and_oscars import leo


@pytest.mark.parametrize('given, expected',[
    (88,"Leo finally won the oscar! Leo is happy"),
    (87,"When will you give Leo an Oscar?"),
    (86,"Not even for Wolf of wallstreet?!")])
def test_leo(given, expected):
    assert leo(given) == expected
