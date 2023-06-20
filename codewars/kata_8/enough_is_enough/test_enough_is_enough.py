from enough_is_enough import delete_nth


def test_delete_nth():
    data_1 = [1, 1, 1, 1]
    expected = [1, 1]
    assert delete_nth(data_1, 2) == expected


def test_delete_nth_2():
    data_1 = [20, 37, 20, 21]
    expected = [20, 37, 21]
    assert delete_nth(data_1, 1) == expected
