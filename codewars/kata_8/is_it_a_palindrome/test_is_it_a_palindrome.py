from is_it_a_palindrome import is_palindrome


def test_is_palindrome1():
    assert is_palindrome('Abba') == True


def test_is_palindrome2():
    assert is_palindrome('Abbas') == False
