"""You are trying to determine which of two apartments has a larger balcony. 
Both balconies are rectangles, and you have the length and width, but you 
need the area.

Task 
Evaluate the area of two different balconies and determine which one is bigger.

Input Format 
Your inputs are two strings where the measurements for height and width are 
separated by a comma. The first one represents apartment A, the second 
represents apartment B.

Output Format: 
A string that says whether apartment A or apartment B has a larger balcony.

Sample Input 
'5,5'
'2,10'

Sample Output 
Apartment A"""


def balcony(balcon_a, balcon_b):
    """Output bigger balcony"""
    balcon_a = balcon_a.split(',')
    balcon_b = balcon_b.split(',')
    a_size = int(balcon_a[0]) * int(balcon_a[1])
    b_size = int(balcon_b[0]) * int(balcon_b[1])
    return ['Apartment B', 'Apartment A'][a_size > b_size]
