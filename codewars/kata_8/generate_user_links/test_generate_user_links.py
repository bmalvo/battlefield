import pytest
from generate_user_links import generate_link


@pytest.mark.parametrize('name, link', [
    ('matt c', 'http://www.codewars.com/users/matt%20c'),
    ('g964', 'http://www.codewars.com/users/g964'),
    ('GiacomoSorbi', 'http://www.codewars.com/users/GiacomoSorbi'),
    ('ZozoFouchtra', 'http://www.codewars.com/users/ZozoFouchtra'),
    ('colbydauph', 'http://www.codewars.com/users/colbydauph')])
def test_generate_link(name, link):
    assert generate_link(name) == link
