import pytest
from easy_logs import logs


@pytest.mark.parametrize('given, expected', [
    ((10, 2, 3), 0.7781512503836436),
    ((5, 2, 3), 1.1132827525593785),
    ((1000, 2, 3), 0.259383750127881237),
    ((2, 1, 2), 1),
    ((0.00001, 0.002, 0.01), 0.9397940008672037),
    ((0.1, 0.002, 0.01), 4.698970004336019)
    ])

def test_logs(given, expected):
    assert logs(given[0], given[1], given[2]) == expected
