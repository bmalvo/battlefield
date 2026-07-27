"""You need to verify if the given credit card number is valid. For that you 
need to use the Luhn test.

Here is the Luhn formula:
1. Reverse the number.
2. Multiple every second digit by 2. 
3. Subtract 9 from all numbers higher than 9.
4. Add all the digits together.
5. Modulo 10 of that sum should be equal to 0. 

Task: 
Given a credit card number, validate that it is valid using the Luhn test. 
Also, all valid cards must have exactly 16 digits.

Input Format:
A string containing the credit card number you need to verify.

Output Format:
A string: 'valid' in case the input is a valid credit card number (passes the 
Luhn test and is 16 digits long), or 'not valid', if it's not.

Sample Input:
4091131560563988

Sample Output:
valid"""


def credit_card_validator(card_number: str) -> str:
    "Check if the given card number is valid"
    test_Luhn_1 = card_number[::-1]
    test_Luhn_2 = [i * 2 for i in test_Luhn_1[::-2]]
    test_Luhn_3 = [i - 9 if i > 9 else i for i in test_Luhn_2]
    test_Luhn_4 = sum(test_Luhn_3)
    return ['invalid', 'valid'][test_Luhn_4 % 10 == 0]

test_list = [1,2,1,2,1,2]

test = sum([i*2 for i in test_list[::-2]])

print(credit_card_validator('4091131560563988'))
