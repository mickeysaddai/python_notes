# error handling
a = 5
try:
    print(len(a))
except:
    print(f'{a} has no length')

# def divide(x, y):
#     try:
#         result = x / y
#     except ZeroDivisionError:
#         print("Cannot divide by zero")
#     else:
#         print("Result is", result)
#     finally:
#         print("Finally...")
# print(divide(10, 5))


def greeting():
    try:
        return "Hey, friend."
    finally:
        return "Fun times!"


print(greeting())