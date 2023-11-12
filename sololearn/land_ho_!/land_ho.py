"""You are on a large ship and you put down anchor near a beautiful beach. 
There is a small boat ferrying passengers back and forth, and you get in line 
for it. How long will you have to wait to get to the beach? You know that 20 
people can fit on the boat and each trip to shore takes 10 minutes each way.

Task: 
Determine your wait time if you know the total number of people ahead of you 
in line.  

Input Format: 
An integer that represents the total number of people ahead of you in line.

Output Format: 
An integer that represents the number of minutes that you will have to wait 
until you are standing on the beach.

Sample Input: 
15

Sample Output: 
10"""


def time_to_get_shore(passengers_ahead):
    """count time to get you to a shore"""
    capacity = 20
    time_one_course = 20
    course_to_shore = 10
    return passengers_ahead // capacity * time_one_course + course_to_shore
