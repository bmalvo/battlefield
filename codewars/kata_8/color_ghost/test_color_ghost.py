from color_ghost import Ghost

def test_ghost_white():
    ghosts = [Ghost().color for i in range(100)]
    assert ghosts.count('white') >= 1

def test_ghost_yellow():
    ghosts = [Ghost().color for i in range(100)]
    assert ghosts.count('yellow') >= 1

def test_ghost_purple():
    ghosts = [Ghost().color for i in range(100)]
    assert ghosts.count('purple') >= 1

def test_ghost_red():
    ghosts = [Ghost().color for i in range(100)]
    assert ghosts.count('red') >= 1
