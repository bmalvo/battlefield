"""If you live in Neverland, you never get any older! You and your twin go to 
Neverland for an afternoon, then your twin goes back home and you stay. Over 
time, how much older is your twin than you, and how old are they?

Task: 
Evaluate the difference between your ages, and the age that your twin is now 
if you are given the age that you were when you got to Neverland, and the time 
that has elapsed since then.

Input Format: 
Two integer values. The first represents your age when you arrived at 
Neverland, and the second, the number of years that have passed since your 
twin went back.

Output Format: 
A string that states 
'My twin is X years old and they are Y years older than me' Where X is their 
age and Y is the difference. 

Sample Input: 
10 
8

Sample Output: 
My twin is 18 years old and they are 8 years older than me"""


def age_counter(my_age, time_passed):
    """output age of my twin and how much time passed"""
    twin_age = my_age + time_passed
    res = (f'My twin is {twin_age} years old and they are '
           f'{time_passed} years older than me')
    return res
