# def add(x, y):
#     print(x + y)
#     return x + y

# result = add(5, 8)
# print(result)

def divide(dividend, divisor):
    if divisor != 0:
        return dividend / divisor
    else:
        return "You fool!"

answer = divide(8, 2)
print(answer)