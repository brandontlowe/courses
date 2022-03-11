# def add(x, y):
#     return x + y

# print(add(7, 2))

# add = lambda x, y: x + y
# print(add(3, 3))


# Doubling with normal function and list comprehension
def double(x):
    return 2 * x

sequence = [1, 3, 5, 7, 9]
doubled = [double(x) for x in sequence]
print(doubled)

# Doubling with lambda function and map
second_doubled = list(map(lambda x: 2 * x, sequence))
print(second_doubled)


