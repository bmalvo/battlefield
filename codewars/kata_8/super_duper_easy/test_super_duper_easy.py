from typing import Literal
import pytest
from super_duper_easy import problem


@pytest.mark.parametrize('given, expected', [("hello", "Error"),
                                             (1, 56)])

def test_problem(given: int, expected: Literal['Error'] | Literal[56]):
    assert problem(given) == expected