# def named(**kwargs):
#     print(kwargs)

# named(name="Bob", age=30)

# def named(name, age):
#     print(name, age)

# details = {"age": 32, "name": "Bob"}
# named(**details)


# def named(**kwargs):
#     print(kwargs)

# def print_nicely(**kwargs):
#     named(**kwargs)
#     for arg, value in kwargs.items():
#         print(f"{arg}: {value}")

# print_nicely(name="Bob", age=25)

# PACKING POSITIONAL AND KEYWORD ARGUMENTS FOR THE SAME FUNCTION

def both(*args, **kwargs):
    print(args)
    print(kwargs)

both(7, 7, 8, forename="David", surname="Cameron")