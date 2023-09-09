from jennys_secret_massage import greet


def test_greet():
    name = 'Jack'
    assert greet(name) == "Hello, Jack!"


def test_greet_if_name_is_johnny():
    name = 'Johnny'
    assert greet(name) == "Hello, my love!"
