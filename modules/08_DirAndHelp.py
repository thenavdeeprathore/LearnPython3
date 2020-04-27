# Finding Members of Module by using dir() Function:
"""
Python provides inbuilt function dir() to list out all members of current module or a specified module.

dir()  To list out all members of current module

dir(moduleName)  To list out all members of specified module
"""


# Eg 1: test.py -- To print all members of current module
"""
x=10
y=20
def f1():
    print("Hello")
    print(dir()) # To print all members of current module


Output:
['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__nam
e__', '__package__', '__spec__', 'f1', 'x', 'y'] 
"""


# Eg 2: To display members of particular module
"""
mymath.py:
x=888

def add(a,b):
    print("The Sum:",a+b)

def product(a,b):
    print("The Product:",a*b)


test.py:
import mymath
print(dir(mymath))


Output:
['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__',
'__package__', '__spec__', 'add', 'product', 'x'] 
"""


# Difference between dir() and help()
"""
dir() --> This 07_functions lists out all members of the given module

help() --> This function provides documentation related to that module
"""

import math

print(dir(math))
print(help(math))


# Note: For every module at the time of execution Python interpreter will add some special
# properties automatically for internal use.
"""
Eg: __builtins__,__cached__,'__doc__,__file__, __loader__, __name__,__package__,__spec__

Based on our requirement we can access these properties also in our program.

print(__doc__)
print(__file__)
print(__name__)
print(__builtins__ )
print(__cached__ )
print(__loader__)
print(__package__)
print(__spec__) 
"""