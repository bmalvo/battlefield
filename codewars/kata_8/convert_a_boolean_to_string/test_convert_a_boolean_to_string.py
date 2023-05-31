from convert_a_boolean_to_string import boolean_to_string

def test_boolean_is_true():
    assert boolean_to_string(True) == "True"

def test_boolean_is_false():
    assert boolean_to_string(False) == "False"

test_boolean_is_false()
test_boolean_is_true()
