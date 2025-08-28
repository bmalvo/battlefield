"""Write a simple function that takes as a parameter a date object and returns 
a boolean value representing whether the date is today or not.

Make sure that your function does not return a false positive by only checking 
the day."""


from datetime import datetime


def is_today(date: datetime) -> bool:
    # your code here
    return  datetime(date).strftime == datetime.today()


# print(is_today((2020, 10, 1, 1, 1, 1, 1)))

print(datetime.today())
