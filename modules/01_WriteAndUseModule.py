# Module
"""
A group of 07_functions, variables and classes saved to a file, is known as module.

Every Python file (.py) acts as a module.
"""

# Imagine this a file named as -- mymath.py
x = 100


def add(a, b):
    print("The Sum:", a + b)


def product(a, b):
    print("The Product:", a * b)


class A:
    pass


"""
mymath.py module contains one variable and 2 07_functions.

If we want to use members of module in our program then we should import that
module.

import modulename

We can access members by using module name.
    modulename.variable
    modulename.function()
"""

# Imagine this is a test file named as -- test.py
import mymath

print(mymath.x)  # 100
mymath.add(10, 20)  # The Sum: 30
mymath.product(10, 20)  # The Product: 200

"""
Module Advantages:
------------------
Code re-usability --> write once use many times
Code readability --> length of the code will be reduced
Maintainability --> Make changes only in one file
"""

# Note 1:
# Whenever we are using a module in our program, for that module compiled file (.pyc)
# will be generated and stored in the folder (__pycache__) permanently.
# 100 test files can use the same one compiled file (mymth.pyc) from the folder (__pycache__)

