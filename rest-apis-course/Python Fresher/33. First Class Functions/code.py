# A first class function is a function you can pass to another
# as an argument
# In the example below, the divide function is passed as a keyword argument
# that is called

# def divide(dividend, divisor):
#     if divisor == 0:
#         raise ZeroDivisionError("Divisor cannot be 0")

#     return dividend / divisor

# def calculate(*values, operator):
#     return operator(*values)

# result = calculate(20, 4, operator=divide)
# print(result)


# Here is another example. It takes a sequence, an expected result, and a
# finder function as arguments. The sequence is iterated over: if the expected
# result is returned when a particular element is passed to the finder,
# then that element is returned.

def search(sequence, expected, finder):
    for elem in sequence:
        if finder(elem) == expected:
            return elem

    raise RuntimeError(f"Could not find an element with {expected}")

# In this specific implementation, the function get_friend_name will operate on
# an array consisting of dictionaries containing data on friends

friends = [
    {"name": "Dave", "age": 33},
    {"name": "Roger", "age": 39}
]

def get_friend_name(friend):
    return friend["name"]

print(search(friends, "Dave", get_friend_name))

# Instead of using a custom function to pass as the finder, this is a great use case
# for itemgetter from the built-in operator module. Calling itemgetter returns a function
# that returns the item with a particular name from a dictionary

from operator import itemgetter

print(search(friends, "Dave", itemgetter("name")))
