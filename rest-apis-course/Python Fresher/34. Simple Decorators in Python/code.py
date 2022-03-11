# Suppose we have a user object. The has an access level of guest
# and guests do not permission to get the password for the admin
# panel, which the function below returns.

user = {"username": "Jose", "access_level": "guest"}

def get_admin_password():
    return "password"

print(get_admin_password())

# Perhaps we could use a modified version of the function, with an if
# statement that returns the password on the condition that the access
# level is "admin"

def get_admin_password_secure():
    if user["access_level"] == "admin":
        return "password"

print(get_admin_password_secure())

# This  requires the addition of an if statement to every
# function that needs to be secured, and impairs the breviety
# of your code

# Here is another idea: you can write a function that returns
# get_admin_password if the user has the required access level

# def secure_function(func):
#     if user["access_level"] == "admin":
#         return func

# get_admin_password = secure_function(get_admin_password)
# print(get_admin_password)

# But this checks the user access level when it is defined:
# not when it is called.

# Instead, let's write a function that returns a secure version
# of the function - i.e. a function that returns a function that
# will call the original function if the user has the required
# access level

def make_secure(func):
    def secure_function():
        if user["access_level"] == "admin":
            return func()
        
    return secure_function

get_admin_password = make_secure(get_admin_password)
print(get_admin_password())
user = {"username": "David", "access_level": "admin"}
print(get_admin_password())

# We now have a simple decorator!