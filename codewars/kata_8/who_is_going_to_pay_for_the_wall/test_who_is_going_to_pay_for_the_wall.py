import pytest
from who_is_going_to_pay_for_the_wall import who_is_paying


@pytest.mark.parametrize('given, expected', [(("Mexico"),["Mexico", "Me"]),
                                             (("Melania"),["Melania", "Me"]),
                                             (("Melissa"),["Melissa", "Me"]),
                                             (("Me"),["Me"]), ((""), [""]),
                                             (("I"), ["I"])])
def test_who_is_paying(given, expected):
    assert who_is_paying(given) == expected
