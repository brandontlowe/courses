# USE * BEFORE PARAMETER TO COLLECT FUNCTION ARGUMENTS INTO A TUPLE
def multiply(*args):
    print(args)
    total = 1
    for arg in args:
        total = total * arg

    return total

print(multiply(1, 2, 3))

# USE * BEFORE ARGUMENT IN THE CALL TO UNPACK THE ARGUMENT SO
# IT IS DESTRUCTURED, IF ARGUMENT IS A LIST/TUPLE

def add(x, y):
    return x + y

nums = [6, 8]
print(add(*nums))

# YOU CAN ALSO DESTRUCTURE A DICTIONARY TO PASS NAMED ARGUMENTS.
# THE ARGUMENT NAMES ARE GIVEN BY THE KEYS

def subtract(x, y):
    return x - y

second_nums = {"y": 7, "x": 2}
print(add(**second_nums))
print(subtract(**second_nums))

