class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # __str__ determines the string that is printed when you pass the object to print
    # __str__ gives a nice, easy-to-understand respresentation for users
    def __str__(self):
        return f"{self.name}, {self.age} years old"

    # By contrast, __repr__() gives a representation that allows object to be easily recreated.
    # Passing the object to print will only call __repr__() if string is not defined
    def __repr__(self):


bob = Person("Bob", 35)
print(bob)