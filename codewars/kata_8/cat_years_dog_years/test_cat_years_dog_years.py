import pytest
from cat_years_dog_years import human_years_cat_years_dog_years


@pytest.mark.parametrize('human_years, appropriate_years', [(1, [1,15,15]),
                                                            (2, [2,24,24]),
                                                            (10, [10,56,64])])
def test_human_years_cat_years_dog_years(human_years, appropriate_years):
    assert human_years_cat_years_dog_years(human_years) == appropriate_years
