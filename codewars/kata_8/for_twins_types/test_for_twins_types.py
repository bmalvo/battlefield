from for_twins_types import type_validation
import pytest


@pytest.mark.parametrize('given, expected',
                         [((42, "int"), True), (("42", "int"), False)])
def test_type_validation(given, expected):
    assert type_validation(given[0], given[1]) == expected
