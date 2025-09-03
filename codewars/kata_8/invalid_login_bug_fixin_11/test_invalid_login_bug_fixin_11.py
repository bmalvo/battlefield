import pytest
from invalid_login_bug_fixin_11 import validate


@pytest.mark.parametrize('given, expected', [
    (('Timmy', 'password'), 'Successfully Logged in!'),
    (('Timmy', 'h4x0r'), 'Wrong username or password!'),
    (('Alice','alice'),'Successfully Logged in!'),
    (('Timmy','password"||""=="'),'Wrong username or password!'),
    (('Admin','gs5bw"||1==1//'),'Wrong username or password!')])
def test_validate(given, expected):
    login, password = given
    assert validate(login, password) == expected
