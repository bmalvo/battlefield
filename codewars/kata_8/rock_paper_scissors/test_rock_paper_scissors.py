from rock_paper_scissors import rps


def test_draw_rps():
    assert rps('rock', 'rock') == 'Draw!'


def test_win_rps():
    assert rps('rock', 'scissors') == 'Player 1 won!'


def test_fail_rps():
    assert rps('rock', 'paper') == 'Player 2 won!'
