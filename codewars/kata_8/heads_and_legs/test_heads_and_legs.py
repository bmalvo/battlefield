import pytest
from heads_and_legs import animals


@pytest.mark.parametrize('given, expected', [((72, 200), (44, 28)),
                                             ((116, 282), (91, 25)),
                                             ((12, 24), (12, 0)),
                                             ((6, 24), (0, 6)),
                                             ((344, 872), (252, 92)),
                                             ((158, 616), (8, 150)),
                                             ((25, 555), "No solutions"),
                                             ((12, 25), "No solutions"),
                                             ((54, 956), "No solutions"),
                                             ((5455, 54956), "No solutions")])
def test_animals(given, expected):
    assert animals(given[0], given[1]) == expected
