# def divide(dividend, divisor):
#     if divisor == 0:
#         print("Divisor cannot be 0")
#         return
    
#     return dividend / divisor

# grades = []

# print("Calculating average grade")
# average = divide(sum(grades), len(grades))

# print(f"The average grade is {average}")

# The divide function is only concerned with mathematics.
# We are not really told that the average grade calculation is unsuccessful -
# we just get that the average grade is "None". This isn't very revealing.

# The program below is slightly better

# def divide(dividend, divisor):
#     return dividend / divisor

# grades = []

# if len(grades) == 0:
#     print("You don't have any grades yet.")
# else:
#     average = divide(sum(grades) / len(grades))
#     print(f"The average grade is {average}")

# Now you get information about how the error relates to the grades, but no information about the root
# programatic or mathematical cause of the error. It also isn't clear that this code is meant for dealing with errors -
# it could well just be another part of the program that could run when everything is happening as expected.

# The "proper" way to deal with this is to raise an error:

# def divide(dividend, divisor):
#     if divisor == 0:
#         # Zero division error is a built-in error type. Its meaning is
#         # self-explanatory
#         raise ZeroDivisionError("Divisor cannot be 0")

#     return dividend / divisor

# grades = []
# average = divide(sum(grades) / len(grades))
# print(f"The average grade is {average}")

# You get a traceback, showing where the error is and why it happened. But you still don't know the root
# programatic cause of the error - the zero division.

# To catch the error, you use a "try and except block". When the error occurs,
# you can use conditioning to give the programmer/tester/yourself extra information
# about why the error happened, i.e. in this case how it relates to the grades.
# You can also assign the exception to a variable which gives you information about the
# programatic or mathematical cause of the error. So you have both: the root cause of the error,
# and how it relates to this part of the program specifically.

# def divide(dividend, divisor):
#     if divisor == 0:
#         raise ZeroDivisionError("Divisor cannot be 0")

#     return dividend / divisor

# grades = []

# try:
#     average = divide(sum(grades) / len(grades))
# except ZeroDivisionError as exception:
#     print(exception)
#     print("There are no grades yet in your list")

# The above prevents the traceback. But it gives information about the cause of the error. If
# the same error in the divide function is raised somewhere there isn't a try-except block,
# you still get the traceback and thus some information about the error. So we have separated the error itself
# - and where it is raised - from how it relates to this specific part of the program, and can get
# information about both.

# Consider the more elaborate example below:

def divide(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("Divisor cannot be 0")

    return dividend / divisor

students = [
    {"name": "Bob", "grades": [75, 90]},
    {"name": "Rolf", "grades": []},
    {"name": "Jen", "grades": [100, 90]}
]

try:
    for student in students:
        name = student["name"]
        grades = student["grades"]
        average = divide(sum(grades), len(grades))
        print(f"{name} averaged {average}")
except ZeroDivisionError:
    # Note that you can have several except clauses for the same try-except block for different error types.
    # So you could have another for RuntimeError.
    print(f"ERROR: {name} has no grades!")
else:
    # Else statement runs when there is no error raised
    print("All student averages calculated")
finally:
    # Runs regardlesss of whether error is raised or not.
    print("End of student average calculation")