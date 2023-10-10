from classy_classes import Person

def test_info():
    ro =  Person('Roman', 36)
    assert ro.info == 'Romans age is 36'
