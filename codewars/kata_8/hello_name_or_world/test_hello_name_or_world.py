from hello_name_or_world import hello


def test_hello_without_arg():
    assert hello() == 'Hello, World!'


def test_hello_with_arg():
    assert hello('John') == 'Hello, John!'
