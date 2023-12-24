from crash_override import alias_gen


class TestAliasCrash:

    def test_m(txt):
        assert alias_gen('Mike', 'Millington') == 'Malware Mike'

    def test_f_t(txt):
        assert alias_gen('Fahima', 'Tash') == 'Function T-Rex'
        
    def test_d_p(txt):
        assert alias_gen('Daisy', 'Petrovic') == 'Data Payload'

    def test_b_w(txt):
        assert alias_gen('Barny', 'White') == 'Beta Worm'

    def test_noalpha(txt):
        assert alias_gen(
            '123abc', 'Pinkman') == 'Your name must start with a letter from A - Z.'
