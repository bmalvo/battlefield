"""Build a function that takes in two arguments (salary, bonus).
Salary will be an integer, and bonus a boolean.

If bonus is true, the salary should be multiplied by 10. If bonus is false, the fatcat did not make
enough money and must receive only his stated salary.

Return the total figure the individual will receive as a string prefixed with "£" (= "\u00A3", JS,
Go, Java, Scala and Julia), "$" (C#, C++, Ruby, Clojure, Elixir, PHP, Python, Haskell and Lua)
or "¥" (Rust)."""


def bonus_time(salary, bonus):
    """Calc salary with achieved bonus if True"""
    return f'${salary*10}' if bonus else f'${salary}'
