# ********Day 54 Start**********
# Functions can have inputs/functionality/output
import time


# def add(n1, n2):
#     return n1 + n2
#
#
# def subtract(n1, n2):
#     return n1 - n2
#
#
# def multiply(n1, n2):
#     return n1 * n2
#
#
# def divide(n1, n2):
#     return n1 / n2
#
#
# Functions are first-class objects, can be passed around as arguments e.g. int/string/float etc.
#
# def calculate(calc_function, n1, n2):
#     return calc_function(n1, n2)
#
#
# result = calculate(add, 2, 3)
# print(result)


# Nested Functions

# def outer_function():
#     print("I am outer")
#
#     def nested_function():
#         print("I am inner")
#
#     nested_function()
#
#
# outer_function()

# Functions can be returned from other functions

# def outer_function():
#     print("I am outer")
#
#     def nested_function():
#         print("I am inner")
#
#     return nested_function
#
#
# inner_function = outer_function()
# inner_function()

# Python Decorator Function

# def delay_decorator(function):
#     def wrapper_function():
#         time.sleep(2)
#         # Do something before
#         function()
#         # Do something after
#     return wrapper_function
#
#
# @delay_decorator
# def say_hello():
#     print("Hello")
#
#
# @delay_decorator
# def say_bye():
#     print("Bye")
#
#
# def say_greeting():
#     print("How are you?")
#
#
# decorated_function = delay_decorator(say_greeting())

## Advanced Python Decorator Functions

class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False


def is_authenticate_decorator(function):
    def wrapper(*args, **kwargs):
        if args[0].is_logged_in:
            function(args[0])
    return wrapper


@is_authenticate_decorator
def create_blog_post(user):
    print(f"This is {user.name}'s new blog post")


new_user = User("Muhaimin")
new_user.is_logged_in = True
create_blog_post(new_user)
