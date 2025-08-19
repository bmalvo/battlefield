import pytest
from sleigh_authentication import Sleigh


@pytest.mark.parametrize('given, expected', [
    (('Santa Claus', 'Ho Ho Ho!'), True),
    (('Santa', 'Ho Ho Ho!'), False )])

def test_sleight(given, expected):
    assert Sleigh.authenticate(given[0], given[1]) == expected
