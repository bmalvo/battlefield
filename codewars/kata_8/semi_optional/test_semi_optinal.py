from semi_optinal import wrap


def test_wrap():
    wrap1 = wrap('test')
    assert wrap1['value'] == 'test'
