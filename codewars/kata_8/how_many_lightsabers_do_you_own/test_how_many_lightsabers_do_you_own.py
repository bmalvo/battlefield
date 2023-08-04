from how_many_lightsabers_do_you_own import how_many_light_sabers_do_you_own


def test_how_many_lightsabers_Zach_arg():
    assert how_many_light_sabers_do_you_own("Zach") == 18


def test_how_many_lightsabers_without_arg():
    assert how_many_light_sabers_do_you_own() == 0


def test_how_many_lightsabers_with_other_arg():
    assert how_many_light_sabers_do_you_own('Bob') == 0
