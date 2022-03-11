user = {"name": "David", "access_level": "admin"}

# Let's define our simple decorator again

# def make_secure(func):
#     def secure_function():
#         if user["access_level"] == "admin":
#             return func()
#         else:
#             print(f'{user["name"]} does not have admin access')

#     return secure_function

# The approach we took in the previous lesson requires us to define the function
# before it is decorated - i.e. it was still insecure up until we called the
# make_secure function

# Instead, we can use the @ syntax to secure the function when it is defined.

# @make_secure
# def get_admin_password():
#     return "password"

# print(get_admin_password())

# But we now have a problem - even though the function is assigned to the variable
# with name get_admin_password, this is not its actual function name. Its name is
# secure_function, as this is what is returned by the decorator. Any documentation
# associated with get_admin_password will also be lost.

# print(get_admin_password.__name__)

# However, we can use another decorator, which comes built-in with the functools module -
# this is the wraps function. We used it to decorate secure_function, so that secure
# function has the same name as the function being secured

import functools

def make_secure(func):
    @functools.wraps(func)
    def secure_function():
        if user["access_level"] == "admin":
            return func()
        else:
            print(f'{user["name"]} does not have admin access')
    
    return secure_function

@make_secure
def get_admin_password():
    return "password"

print(get_admin_password.__name__)
print(get_admin_password())