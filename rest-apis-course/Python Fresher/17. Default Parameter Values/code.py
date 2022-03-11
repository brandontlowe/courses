# def add(x, y=8):
#     print(x + y)

# add(5, y=5)

default_y=3

def add(x, y=default_y):
    print(x + y)

add(2)

default_y = 4
add(2)  # THIS GIVES THE SAME VALUE AS BEFORE EVEN THOUGHT DEFAULT_Y HAS CHANGED.

# This is because the default parameter values are static and fixed
# once the function is defined