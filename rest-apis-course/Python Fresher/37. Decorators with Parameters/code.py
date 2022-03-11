import functools

user = {"name": "Derek", "access_level": "admin"}

# def make_secure(func):
#     @functools.wraps(func)
#     def secure_function(*args, **kwargs):
#         if user["access_level"] == "admin":
#             return func(*args, **kwargs)
    
#     return secure_function

# @make_secure
# def get_admin_password():
#     return "admin: password"

# @make_secure
# def get_user_password():
#     return "user: 1234"

# We have two functions, both of which have been secured with the decorator. Suppose we want the admin password
# to only be accessible by admins and the user password to only be accessible by users. The decorator we have
# been using so far always checks for admin access level.

# If we want to be able to customise the required access level, we must nest the decorator in another function.
# This function accepts a parameter, and returns a decorator - the decorator changes based on the value of the
# argument.

def make_secure(access_level):
    def decorator(func):
        @functools.wraps(func)
        def secure_function():
            if user["access_level"] == access_level:
                return func()

        return secure_function    
    
    return decorator

# Now we can use this "decorator factory" to customise our decorators. Instead of decorating functions
# to be secured with the decorator directly, we decorate them with a call to make_secure(), or the factory,
# which returns the decorator.

@make_secure("admin")
def get_admin_password():
    return "admin: password"

@make_secure("user")
def get_user_password():
    return "user: 1234"

print(get_admin_password())
print(get_user_password())

user = {"name": "Jesus", "access_level": "user"}

print(get_user_password())