import pytest
from fix_the_loop import list_animals


@pytest.mark.parametrize('given, expected', [
    (['dog', 'cat', 'elephant'], '1. dog\n2. cat\n3. elephant\n'),
    ([ 'bird', 'parrot', 'elephant', 'giraffe'], '1. bird\n2. parrot\n3. elephant\n4. giraffe\n'),
    ([ 'pig', 'frog', 'hamster', 'mouse', 'sloth'], '1. pig\n2. frog\n3. hamster\n4. mouse\n5. sloth\n'),
    ([ 'cow', 'horse', 'pig', 'donkey', 'buffalo', 'turtle', 'chicken' ], '1. cow\n2. horse\n3. pig\n4. donkey\n5. buffalo\n6. turtle\n7. chicken\n')])
def test_list_animals(given, expected):
    assert list_animals(given) == expected
