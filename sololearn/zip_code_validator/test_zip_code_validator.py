from zip_code_validator import code_validator
import pytest


@pytest.mark.parametrize('given, expected', [('752f78', False),
                                             ('52452', True),
                                             ('424', False)])
def test_code_validator(given, expected):
    assert code_validator(given) == expected
