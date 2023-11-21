from gotham_city import call_out_batman
import pytest


@pytest.mark.parametrize('given, expected', [(4, 'I got this!'),
                                             (10, 'Help me Batman'),
                                             (11, 'Good Luck out there!')])
def test_call_out_batman(given, expected):
    assert call_out_batman(given) == expected
