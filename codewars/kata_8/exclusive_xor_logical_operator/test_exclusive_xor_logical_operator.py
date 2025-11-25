import pytest
from exclusive_xor_logical_operator import xor


@pytest.mark.parametrize('given, exception',[
    ((False, False), False),
    ((True, False), True),
    ((False, True), True),
    ((True, True), False)
])

def test_xor(given, exception):
    a, b = given
    assert xor(a, b) == exception