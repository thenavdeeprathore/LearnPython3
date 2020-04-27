"""
Nested Functions:
----------------
=>  We can declare a function inside another function, such type of functions are called Nested functions.

Note: A function can return another function.
"""


# case 1:
def outer():
    print("outer function")

    def inner():
        print("inner function")

    print("outer function calling inner function")
    inner()


outer()
# outer function
# outer function calling inner function
# inner function


# NOTE: In the above example inner() function is local to outer() function and hence it is not
# possible to call directly from outside of outer() function.


# case 2:
def outer():
    print("outer function")

    def inner():
        print("inner function")

    print("outer function calling inner function")
    return inner


# aliasing
f1 = outer
f1()
# outer function
# outer function calling inner function


# inner function() we are providing another name f1
f1 = outer()
f1()
# outer function
# outer function calling inner function
# inner function
f1()
# inner function
f1()
# inner function


'''
Q) What is the difference between the following lines?
    f1 = outer
    f1 = outer()
=>  In the first case for the outer() function we are providing another name f1
    (function aliasing).
=>  But in the second case we calling outer() function, which returns inner function.
    For that inner function() we are providing another name f1
'''
