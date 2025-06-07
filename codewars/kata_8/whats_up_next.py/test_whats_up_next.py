from whats_up_next import next_item


def test_next_item_1():
    assert next_item([1, 2, 3, 4, 5, 6, 7], 3) == 4


def test_next_item_2():
    assert next_item(['Joe', 'Bob', 'Sally'], 'Bob') == 'Sally'


def test_next_item_3():
    assert next_item(['a', 'b', 'c'], 'd') == None


def test_next_item_4():
    assert next_item(['a', 'b', 'c'], 'c') == None
