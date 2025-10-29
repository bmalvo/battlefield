import pytest 
from grade_book import get_grade


@pytest.mark.parametrize('given, expected', [
    ((95, 90, 93), "A"),
    ((100, 85, 96), "A"),
    ((92, 93, 94), "A"),
    ((100, 100, 100), "A"),
    ((70, 70, 100), "B"),
    ((82, 85, 87), "B"),
    ((84, 79, 85), "B"),
    ((70, 70, 70), "C"),
    ((75, 70, 79), "C"),
    ((60, 82, 76), "C"),
    ((65, 70, 59), "D"),
    ((66, 62, 68), "D"),
    ((58, 62, 70), "D"),
    ((44, 55, 52), "F"),
    ((48, 55, 52), "F"),
    ((58, 59, 60), "F",),
    ((0, 0, 0), "F",)])

def test_get_grade(given, expected):
    s1,s2,s3 = given
    assert get_grade(s1, s2, s3) == expected