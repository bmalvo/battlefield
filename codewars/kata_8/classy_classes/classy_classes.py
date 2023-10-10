"""Your task is to complete this Class, the Person class has been created. 
You must fill in the Constructor method to accept a name as string and an age 
as number, complete the get Info property and getInfo method/Info getter which 
should return johns age is 34"""


class Person:
    """Create persons"""
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        self.info=f"{self.__name}s age is {self.__age}"
