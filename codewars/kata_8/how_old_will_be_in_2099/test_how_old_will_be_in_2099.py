import pytest
from how_old_will_be_in_2099 import calculate_age


@pytest.mark.parametrize("birth_year, current_year, output",[
                        (2012, 2016,"You are 4 years old."),
                        (1989, 2016,"You are 27 years old."),
                        (2000, 2090,"You are 90 years old."),
                        (2000, 1990, "You will be born in 10 years."),
                        (2000, 2000,"You were born this very year!"),
                        (900, 2900,"You are 2000 years old."),
                        (2010, 1990,"You will be born in 20 years."),
                        (2010, 1500,"You will be born in 510 years."),
                        (2011, 2012,"You are 1 year old."),
                        (2000, 1999, "You will be born in 1 year.")])
def test_calculate_age(birth_year, current_year, output):
    assert calculate_age(birth_year, current_year) == output
