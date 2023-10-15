"""Given two strings comprised of + and -, return a new string which shows 
how the two strings interact in the following way:

When positives and positives interact, they remain positive.
When negatives and negatives interact, they remain negative.
But when negatives and positives interact, they become neutral, and are shown 
as the number 0.

Example :
("+-+", "+--") ➞ "+-0"

# Compare the first characters of each string, then the next in turn.
# "+" against a "+" returns another "+".
# "-" against a "-" returns another "-".
# "+" against a "-" returns "0".
# Return the string of characters.

Examples:
("--++--", "++--++") ➞ "000000"

("-+-+-+", "-+-+-+") ➞ "-+-+-+"

("-++-", "-+-+") ➞ "-+00"

The two strings will be the same length."""

def neutralise(signs_1, signs_2):
    """compare characters and return appropriate sign"""

    res = ''

    for i in range(len(signs_1)):
        compare = signs_1[i] + signs_2[i]
        if compare in ('+-', '-+'):
            res += '0'
        elif compare == '--':
            res += '-'
        else:
            res += '+'
    return res
