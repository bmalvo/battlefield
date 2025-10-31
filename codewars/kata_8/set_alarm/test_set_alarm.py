import pytest
from set_alarm import set_alarm


@pytest.mark.parametrize('given, expected', [
    ((True, True), False,),
    ((False, True), False,),
    ((False, False), False,),
    ((True, False), True,)
])
def test_set_alarm(given, expected):
    employed, vacation = given
    assert set_alarm(employed, vacation) == expected
