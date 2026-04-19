import pytest
from grasshopper_combine_strings import combine_names


@pytest.mark.parametrize('given, expected', [
    ("James", "Stevens", "James Stevens"),
    ("Davy", "Back", "Davy Back"),
    ("Arthur", "Dent", "Arthur Dent")
])

def test_combine_names(given, expected):
    assert combine_names(given) == expected
