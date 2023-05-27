import pytest
from byte_me import total_bytes


@pytest.mark.parametrize('given, expect',
                         [("¡◢龘", 80), (999_999, 28), ((1, 2), 56)])
def test_byte_me(given, expect):
    assert total_bytes(given) == expect
