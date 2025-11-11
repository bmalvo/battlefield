import pytest
from my_head_is_at_the_wrong_end import fix_the_meerkat


@pytest.mark.parametrize('given, expected', [
    (["tail", "body", "head"], ["head", "body", "tail"]),
    (["tails", "body", "heads"], ["heads", "body", "tails"]),
    (["bottom", "middle", "top"], ["top", "middle", "bottom"]),
    (["lower legs", "torso", "upper legs"], ["upper legs", "torso", "lower legs"]),
    (["ground", "rainbow", "sky"], ["sky", "rainbow", "ground"])
])

def test_fix_the_meerkat(given, expected):
    assert fix_the_meerkat(given) == expected
