"""You sell souvenir kaleidoscopes at a gift shop, and if a customer buys more
than one, they get a 10% discount on all of them!
Given the total number of kaleidoscopes that a customer buys, let them know 
what their total will be. Tax is 7%. All of your kaleidoscopes cost the same
amount, 5.00.
Take the number of kaleidoscopes that a customer buys and output their total 
cost including tax and any discounts

Input:
An integer value that represents the number of kaleidoscopes that a customer
orders.

Output:
A number that represents the total purchase price to two decimal places."""

DISCOUNT = 0.1
TAX = 0.07
KALEIDOSCOPES_PRIZE = 5.00


def total_cost(kaleidoscopes:int):
    """Return total cost of souvenirs"""
    total = (kaleidoscopes * KALEIDOSCOPES_PRIZE) + kaleidoscopes * KALEIDOSCOPES_PRIZE * TAX
    if kaleidoscopes > 1:
        total = total - (total * DISCOUNT)
    return round(total, 2)
