import pytest
from kata_example_twist import websites


def test_websites():
    assert len(websites) == 1000
