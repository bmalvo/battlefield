import pytest
from welcome import greet


@pytest.mark.parametrize('given, expected',[
    ('english', 'Welcome'),
    ('dutch', 'Welkom'),
    ('IP_ADDRESS_INVALID', 'Welcome'),
    ('', 'Welcome'),
    (2, 'Welcome')
])

def test_greet(given, expected):
    assert greet(given)  == expected