import pytest
from exclamation_mark_series_4 import remove


class TestRemove:


    def setup_method(self, method):
        print(f'setting up {method}')

    def test_1(self):
        assert remove('abc!!!') == 'abc!'

    def test_2(self):
        assert remove('Hi!') == 'Hi!'

    def test_3(self):
        assert remove('Hi!!!') == 'Hi!'

    def test_4(self):
        assert remove('!Hi') == 'Hi!'

    def test_5(self):
        assert remove('!Hi!') == 'Hi!'

    def test_6(self):
        assert remove('Hi! Hi!') == 'Hi Hi!'

    def test_7(self):
        assert remove('Hi') == 'Hi!'
