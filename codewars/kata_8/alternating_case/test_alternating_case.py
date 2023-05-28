from alternating_case import to_alternating_case


def test_to_alternating_case_1():
    given = 'altERnaTIng cAsE'
    assert to_alternating_case(given) == 'ALTerNAtiNG CaSe'

def test_to_alternating_case_2():
    given = 'SECOND TEST'
    assert to_alternating_case(given) == 'second test'
