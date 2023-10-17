from up_and_down_the_string_grows import strange_string

def test_strange_string_false():
    assert strange_string('A') == False

def test_strange_string_true():
    assert strange_string('ᾉ') == True
    