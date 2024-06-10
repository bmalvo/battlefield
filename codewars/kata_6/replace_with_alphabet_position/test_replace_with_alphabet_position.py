from replace_with_alphabet_position import alphabet_position


def test_alphabet_position():
    txt = "The sunset sets at twelve o' clock."
    expected = '20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11'
    assert alphabet_position(txt) == expected


def test_alphabet_position2():
    txt = 'abcdefg'
    expected = '1 2 3 4 5 6 7'
    assert alphabet_position(txt) == expected
