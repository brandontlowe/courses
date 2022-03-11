def add(x, y):
    result = x + y
    print(result)

add(3, 7)

# The above function call uses positional arguments. You can
# also use named/keyword arguments

def say_hello(name, surname):
    print(f"Hello, {name} {surname}")

say_hello(surname="Smith", name="John")