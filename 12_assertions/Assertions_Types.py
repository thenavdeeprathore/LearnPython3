"""
Types of assert Statements:

There are 2 types of assert statements
1) Simple Version
2) Augmented Version


1) Simple Version:
assert conditional_expression


2) Augmented Version:
assert conditional_expression, message

- conditional_expression will be evaluated and if it is true then the program will be continued.
- If it is false then the program will be terminated by raising AssertionError.
- By seeing AssertionError, programmer can analyze the code and can fix the problem.
"""


def square_number(x):
    return x**x  # here is the bug, it should be x*x


print(square_number(2))
assert square_number(2) == 4
print(square_number(2))
assert square_number(2) == 4, "The square of 2 should be 4"
print(square_number(3))
assert square_number(3) == 9, "The square of 3 should be 9"


# how to disable assert statements in python?
# By using -O option

# py test.py ==> Assert statements will be executed
# py -O test.py ==> Assert statements won't be executed

"""
Exception Handling vs Assertions:

Assertions concept can be used to alert programmer to resolve development time errors.

Exception Handling can be used to handle runtime errors.
"""

