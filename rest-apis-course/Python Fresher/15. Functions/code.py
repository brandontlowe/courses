# def hello():
#     print("Hello!")

# hello()

# def user_age_in_seconds():
#     user_age = int(input("Enter your age: "))
#     age_seconds = int(user_age * 365.25 * 24 * 60 * 60)
#     print(f"Your age in seconds is {age_seconds}")

# user_age_in_seconds()

friends = ["Elizabeth", "Ross"]

def add_friend():
    friend_name = input("Enter your friend name: ")
    # This will cause an error in Python - creates new local
    # variable called friend, and you are attempting to use it before it is defined
    # friends = friends + [friend_name]
    # So in Python, using assingment in this way will always create a new local variable
    # 
    # But you can use a new variable name, and 'friends' will still refer to the
    # variable in the global scope
    new_friends = friends + [friend_name]
    print(new_friends)

add_friend()

# FUNCTIONS ARE NOT HOISTED IN PYTHON