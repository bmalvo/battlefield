from if_you_cant_sleep_count_sheep import count_sheep


def test_count_sheep_0():
    assert count_sheep(0) == ""


def test_count_sheep_1():
    assert count_sheep(1) == "1 sheep..."


def test_count_sheep_3():
    assert count_sheep(3) == "1 sheep... 2 sheep... 3 sheep..."
