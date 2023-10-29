from cheer_creator import cheer


def test_cheer_5():
    assert cheer(5) == 'Ra!Ra!Ra!Ra!Ra!'


def test_cheer_0():
    assert cheer(0) == 'shh'

def test_cheer_11():
    assert cheer(11) == 'High Five'
    