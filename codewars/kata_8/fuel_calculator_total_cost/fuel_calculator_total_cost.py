"""In this kata you will have to write a function that takes litres and 
price_per_litre (in dollar) as arguments.

Purchases of 2 or more litres get a discount of 5 cents per litre, purchases 
of 4 or more litres get a discount of 10 cents per litre, and so on every two 
litres, up to a maximum discount of 25 cents per litre. But total discount 
per litre cannot be more than 25 cents. Return the total cost rounded to 2 
decimal places. Also you can guess that there will not be negative or 
non-numeric inputs.

Good Luck!"""


def fuel_price(litres: int, price_per_litre: float) -> float:
    """output total cost of fuel"""
    discount = (litres//2) * 0.05 if litres < 11 else 0.25
    return round(litres * (price_per_litre - discount),2)
