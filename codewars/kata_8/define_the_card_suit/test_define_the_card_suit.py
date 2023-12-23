import pytest
from define_the_card_suit import define_suit


class TestDefineSuit:


    def test_define_suit_clubs(card):
        assert define_suit('3C') == 'clubs'

    def test_define_suit_diamonds(card):
        assert define_suit('3D') == 'diamonds'


    def test_define_suit_hearts(card):
        assert define_suit('3H') == 'hearts'


    def test_define_suit_spades(card):
        assert define_suit('3S') == 'spades'

    def test_define_suit_incorrect(card):
        assert define_suit('3Q') == 'incorrect input'
