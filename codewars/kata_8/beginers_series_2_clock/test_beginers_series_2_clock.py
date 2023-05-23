from beginers_series_2_clock import past
import pytest


@pytest.mark.parametrize('given, expected',
                         [((0, 1, 1), 61000), ((1, 1, 1), 3661000), ((0, 0, 0), 0),
                          ((1, 0, 1), 3601000), ((1, 0, 0), 3600000)])
def test_past(given, expected):
    assert past(given[0], given[1], given[2]) == expected
