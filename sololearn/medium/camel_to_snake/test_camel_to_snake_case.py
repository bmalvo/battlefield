from camel_to_snake import camel_to_snake


def test_camel_to_snake1():
    assert camel_to_snake('SomeName') == 'some_name'


def test_camel_to_snake2():
    assert camel_to_snake('camelCasing') == 'camel_casing'


def test_camel_to_snake3():
    assert camel_to_snake('_camelCasing') == 'camel_casing'
