import pytest
from basic_subclasses_adam_and_eve import *


def test_first_object_is_man():
    paradise = God()
    assert isinstance(
        paradise[0], Man), "First object should be an instance of Man"
