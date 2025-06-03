from name_your_python import Python


def test_python_name():
    """
    Tests if the name attribute is correctly set in the Python class.
    """
    bubba = Python("Bubba")
    assert bubba.name == "Bubba"
