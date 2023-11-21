from duct_tape import rolls_tape_needed
import pytest


@pytest.mark.parametrize('given, expected',[((7, 4), 6),
                                            ((10, 5), 10),
                                            ((6, 3), 4)])
def test_rools_tape_needed(given, expected):
    assert rolls_tape_needed(given[0], given[1]) == expected
