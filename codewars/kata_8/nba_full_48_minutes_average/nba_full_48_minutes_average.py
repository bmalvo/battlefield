"""An NBA game runs 48 minutes (Four 12 minute quarters). Players do not 
typically play the full game, subbing in and out as necessary. Your job is 
to extrapolate a player's points per game if they played the full 48 minutes.

Write a function that takes two arguments, ppg (points per game) and mpg 
(minutes per game) and returns a straight extrapolation of ppg per 48 minutes 
rounded to the nearest tenth. Return 0 if 0."""
# from decimal import ROUND_HALF_UP as round
from math import trunc, floor

def nba_extrap(ppg, mpg):
    """returns a extrapolation of ppg per 48 minutes"""
    # ppg = round(int(ppg))
    # mpg = round(int(mpg))
    if int(mpg) != 0:
        extra_mpg = 48 / mpg
        # print('ekstra: ', extra_mpg)
        result = ppg * extra_mpg 
        # print('result: ', result)
    return 0 if int(mpg) == 0 else int(result * 10) / 10

print(nba_extrap(12,20)) # 28,8
print(nba_extrap(10, 10)) # 48,0
print(nba_extrap(5, 17)) # 14.1
print(nba_extrap(30.8, 34.7)) # 42.6
print(nba_extrap(0, 0))

print(nba_extrap(34.56673075272463, 1.9521223528113634))  # 849.9
