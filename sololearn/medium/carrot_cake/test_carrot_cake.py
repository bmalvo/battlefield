from carrot_cake import divide_carrots


def test_divide_carrots_negative():
    assert divide_carrots(100, 10) == 'I need to buy 7 more'


def test_divide_carrots_negative_2():
    assert divide_carrots(80005, 400) == 'I need to buy 2 more'


def test_divide_carrots_possitive():
    assert divide_carrots(107, 10) == 'Cake Time'
