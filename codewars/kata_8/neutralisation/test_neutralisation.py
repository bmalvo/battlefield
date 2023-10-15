from neutralisation import neutralise
import pytest

@pytest.mark.parametrize('given, expected',[(("+-+", "+--"), "+-0"),
                                            (("--++--", "++--++"),"000000"),
                                            (("-+-+-+", "-+-+-+"),"-+-+-+"),
                                            (("-++-", "-+-+"),"-+00")])
def test_neutralise(given, expected):
    assert neutralise(given[0], given[1]) == expected
