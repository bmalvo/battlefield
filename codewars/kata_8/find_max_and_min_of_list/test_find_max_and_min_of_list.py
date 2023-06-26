from find_max_and_min_of_list import maximum, minimum


def test_maximum():
    given = [1, 2, 3, 4, 5]
    assert maximum(given) == 5


def test_minimum():
    given = [1, 2, 3, 4, 5]
    assert minimum(given) == 1
