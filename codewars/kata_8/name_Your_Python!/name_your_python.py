"""For those of us who are not very familiar with Python, let's handle the very 
basic challenge of creating a class named Python. We want to give our Pythons 
a name, so it should take a name argument that we can retrieve later."""

class Python:
    """Python class with Your name"""
    def __init__(self, name):
        self.name = name

    def greet(self):
        """for greetings"""
        return f"Hello, {self.name}!"

    def get_name(self):
        """gives name"""
        return self.name


bubba = Python('bubba')

print(bubba.name)
