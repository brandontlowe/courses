user = {"name": "David", "access_level": "admin"}

import functools

# def make_secure(func):
#     @functools.wraps(func)
#     def secure_function():
#         if user["access_level"] == "admin":
#             return func()
#         else:
#             print(f'{user["name"]} does not have admin access')
    
#     return secure_function

# @make_secure
# def get_admin_password():
#     return "password"

# Let's replace the get_admin_password() function from last lesson with a more generic
# get_password function, that takes a parameter - the panel to be accessed.

# For this to work we have to modify make_secure so that secure_function and the function
# being decorated both take a parameter - else we will get an error, because the secure_function
# will be expecting 0 paramaters and so will the call to the function being decorated (func())

# def make_secure(func):
#     @functools.wraps(func)
#     def secure_function(panel):
#         if user["access_level"] == "admin":
#             return func(panel)
#         else:
#             print(f'{user["name"]} does not have admin access')
    
#     return secure_function

# @make_secure
# def get_password(panel):
#     if panel == "admin":
#         return "password"
#     elif panel == "billing":
#         return "super_secure_password"

# print(get_password("billing"))

# But now we have limited the use of make_secure() to functions that have 1 parameter - it will not
# work with functions with a different number of params. Furthermore, we have called the parameter panel -
# we have limited its use to decoratoring the get_password() function.

# Fortunately, as we learnt before, we can use argument destructuring so that the the secure_function() can
# accept any number of arguments, and any number of arguments can be passed to the call of the original
# function in secure_function()

def make_secure(func):
    @functools.wraps(func)
    def secure_function(*args, **kwargs):
        if user["access_level"] == "admin":
            return func(*args, **kwargs)
        else:
            print(f'{user["name"]} does not have admin access')
    
    return secure_function

@make_secure
def get_password(panel):
    if panel == "admin":
        return "password"
    elif panel == "billing":
        return "super_secure_password"

print(get_password("billing"))