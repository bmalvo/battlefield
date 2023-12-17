from buildings_blocks import distribute_blocks


def test_distribute_blocks_1():
    assert distribute_blocks(150, 20, 300, 53) == 13


def test_distribute_blocks_2():
    assert distribute_blocks(29, 28, 17, 20) == 34


def test_distribute_blocks_3():
    assert distribute_blocks(300, 150, 300, 300) == 0
