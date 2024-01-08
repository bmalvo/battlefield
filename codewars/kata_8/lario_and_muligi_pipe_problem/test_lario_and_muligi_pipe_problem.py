import pytest
from lario_and_muligi_pipe_problem import pipe_fix


@pytest.mark.parametrize('bust_list, fixed_list', [
    ([1, 2, 3, 5, 6, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9]),
    ([1, 2, 3, 12], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]),
    ([6, 9], [6, 7, 8, 9]),
    ([-1, 4], [-1, 0, 1, 2, 3, 4]),
    ([1, 2, 3], [1, 2, 3])])
def test_pipe_fix(bust_list, fixed_list):
    assert pipe_fix(bust_list) == fixed_list
