import pytest
from pete_the_baker import cakes


@pytest.mark.parametrize('given, expected', 
        [(({'apples': 3, 'flour': 300, 'sugar': 150, 'milk': 100, 'oil': 100},
        {'sugar': 500, 'flour': 2000, 'milk': 2000}), 0),
        (({'flour': 500, 'sugar': 200, 'eggs': 1},
          {'flour': 1200, 'sugar': 1200, 'eggs': 5, 'milk': 200}), 2),
        (({'milk': 97, 'eggs': 5, 'oil': 15},
      {'cream': 8485, 'flour': 6178, 'pears': 8284, 'milk': 75, 'apples': 501,
          'chocolate': 6635, 'eggs': 6820,
          'sugar': 5697, 'cocoa': 1983, 'oil': 7990}), 0),
        (({'cream': 69, 'oil': 47, 'cocoa': 49},
          {'milk': 6863, 'pears': 6551, 'apples': 9098, 'cream': 9223,
          'nuts': 1029, 'flour': 614, 'eggs': 8499,
          'oil': 4662, 'sugar': 8729, 'cocoa': 2700}), 55),
        (({'cream': 200, 'flour': 300, 'sugar': 150, 'milk': 100, 'oil': 100},
          {'sugar': 1700, 'flour': 20000, 'milk': 20000, 'oil': 30000,
          'cream': 5000}), 11)])
def test_cake(given, expected):
    assert cakes(given[0], given[1]) == expected
