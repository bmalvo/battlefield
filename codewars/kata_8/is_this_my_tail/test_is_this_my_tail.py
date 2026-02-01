import pytest
from is_this_my_tail import correct_tail


@pytest.mark.parametrize('given, expected',[
    (("Fox", "x"), True),
    (("Rhino", "o"), True),
    (("Meerkat", "t"), True),
    (("Emu", "t"), False),
    (("Badger", "s"), False),
    (("Giraffe", "d"), False)
])

def test_correct_tail(given, expected):
    animal, tail = given[0], given[1]
    assert correct_tail(animal, tail) == expected