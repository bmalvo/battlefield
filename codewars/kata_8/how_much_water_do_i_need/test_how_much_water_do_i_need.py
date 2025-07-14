from how_much_water_do_i_need import how_much_water


def test_too_much_clothes():
    assert how_much_water(10, 10, 21) == 'Too much clothes'

def not_enough_clothes():
    assert how_much_water(10, 10, 2) == 'Not enough clothes'

def how_much_water_1():
    assert how_much_water(10, 11, 20) == 23.58

def how_much_water_2():
    assert how_much_water(50, 15, 29) == 189.87
