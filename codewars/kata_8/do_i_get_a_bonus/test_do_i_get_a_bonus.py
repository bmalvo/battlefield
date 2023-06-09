from do_i_get_a_bonus import bonus_time


def test_bonus_time_true():
    assert bonus_time(10, True) == '$100'


def test_bonus_time_false():
    assert bonus_time(10, False) == '$10'
