"""Oh NO! Timmy has moved divisions... but now he's in the field of security. 
Timmy, being the top coder he is, has allowed some bad code through. 
You must help Timmy and filter out any injected code!

Task
Your task is simple, search the password string for any injected code 
(Injected code is any thing that would be used to exploit flaws in the current 
code, so basically anything that contains || or //) if you find any you must 
return "Wrong username or password!" because no one likes someone trying to 
cheat their way in!

Preloaded
You will be given a preloaded class called Database with a method login this 
takes two parameters username and password. This is a generic login function 
which will check the database for the user it will return either 
'Successfully Logged in!' if it passes the test or 
'Wrong username or password!' if either the password is wrong or username 
does not exist.

Usage
database = Database()
database.login('Timmy', 'password')"""

class Database:
    """Represents a simple database for user authentication."""

    database = {
        'Timmy': 'password', 
        'Alice': 'alice'}

    def login(self, username, password) -> str:
        """Checks if the username and password are valid."""
        if username in self.database and password == self.database.get(username):
            return 'Successfully Logged in!'
        return 'Wrong username or password!'

    def quantity(self):
        """return amount of the database users"""
        return len(self.database)


def validate(username: str, password: str) -> str:
    """validate input data"""
    database = Database()
    return database.login(username, password)
