import pytest
from hundred_one_dalmatians_squash_the_bugs_not_the_dogs import how_many_dalmatians


@pytest.mark.parametrize('given, expected', [
    ((26), "More than a handful!"),
    ((8), "Hardly any"),
    ((14), "More than a handful!"),
    ((80), "Woah that's a lot of dogs!"),
    ((100), "Woah that's a lot of dogs!"),
    ((50), "More than a handful!"),
    ((10), "Hardly any"),
    ((101), "101 DALMATIONS!!!")
])
def test_how_many_dalmatains(given, expected):
    assert how_many_dalmatians(given) == expected
