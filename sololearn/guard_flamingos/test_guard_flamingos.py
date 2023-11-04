from guard_flamingos import flamingos_needed
import pytest


@pytest.mark.parametrize('given, expected', [((10, 10), 20),
                                             ((30, 100), 130),
                                             ((8, 20), 28)])
def test_flamingos_needed(given, expected):
    assert flamingos_needed(given[0], given[1]) == expected
