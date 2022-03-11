from re import A


a = []
b = a

# Because arrays are reference datatypes, assigning an array that has already been defined to another variable
# does not just copy the content: it copies the reference, so they point to the same array in memory.

print(id(a))
print(id(b))

a.append(35)
print(a)
print(b)

# By contracts, if we assign newly created arrays to a and b, they will have difference IDs: they will
# point to different locations in memory.

a = []
b = []

print(id(a))
print(id(b))

# We can see that a list is mutable - we can change the properties of the object. In Python, most
# variables are mutable because all data types are objects: the only exceptions are data types for
# which we have no way of mutating the object properties.

# An example of an immutable data type is the tuple. Tuples have no methods that can mutate them, nor do
# any operators mutate them.

# Consider integers. If we assign a and b to the same integer value, their IDs will be the same.

a = 301
b = 301

print(id(a))
print(id(b))

# This is because all variables in Python are references. If we assign two variables to the same integer value,
# both references will point to the same object. It is NOT the case that a new object is created. But that
# does not matter, because integers are immutable: we cannot change the value of the object representing
# 301, it is not the case that we can change the value of a by altering the value of b.

# Tuples, strings, integers, floats and booleans are the immutable datatypes in Python. If you want to create
# a custom immutable class or object, then just don't add any methods that can change its properties. The
# properties must also belong to immutable primitive data types, of course.

a = "hello"
b = a

print(id(a))
print(id(b))

# Note that the increment or "+=" operator in Python is actually an abbreviation of a reassignment. I.e.
# b += 1 is b = b + 1. So in this example, using it for a string will create a new string, and reassign the
# variable to that string. It does not mutate the original string.

b += "there"
print(id(a))
print(id(b))