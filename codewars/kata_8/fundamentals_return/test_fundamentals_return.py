from fundamentals_return import add, multiply, divide, mod, exponent, subt


a, b = 1, 2

def test_add():
    assert add(a, b) == 3

def test_multiply():
    assert multiply(a, b) == 2

def test_divide():
    assert divide(a, b) == 0.5

def test_mod():
    assert mod(a, b) == 1

def test_exponent():
    assert exponent(a, b) == 1

def test_subt():
    assert subt(a, b) == -1