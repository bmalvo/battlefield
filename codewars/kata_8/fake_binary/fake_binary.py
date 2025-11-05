"""Given a string of digits, you should replace any digit below 5 with '0' 
and any digit 5 and above with '1'. Return the resulting string."""


def fake_bin(x):
    """change digits to fake binary"""
    binary = ['0' if int(i) < 5 else '1' for i in x]
    return ''.join(binary)
