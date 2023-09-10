from name_on_bilboard import billboard
import pytest


@pytest.mark.parametrize('given, expected',
            [(("Jeong-Ho Aristotelis"), 600), (("Abishai Charalampos"), 570),
             (("Idwal Augustin"), 420), (("Zoroaster Donnchadh"), 570),
             (("Claude Miljenko"), 450), (("Anani Fridumar"), 420), 
             (("Paolo Oli"), 270), (("Simon Eadwulf"), 390)])

def test_billboard_one_param(given, expected):
    assert billboard(given) == expected


@pytest.mark.parametrize('given, expected',
                    [(("Hadufuns John", 20), 260), (("Werner Vigi", 15), 165),
                     (("Hjalmar Liupold", 40), 600)])

def test_billboard_two_param(given, expected):
    assert billboard(given[0], given[1]) == expected
