import pytest
from ensure_question import ensure_question


@pytest.mark.parametrize('enter, output',[('Yes?', 'Yes?'),('No', 'No?')])
def test_ensure_question(enter, output):
    assert ensure_question(enter) == output
