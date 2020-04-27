# try-except-else-finally
"""
1) try block compulsory should have either except or finally block
2) except without try in Invalid
3) finally without try is Invalid
4) else without except is Invalid
5) We can take multiple except blocks
    - but try, else, finally can be only taken one
6) try-except-else-finally order is important
7) We can take try-except-else-finally inside try, except, else, finally blocks
    - Nesting of try-except-else-finally is possible
8) else block will execute always if there is NO exception
"""

# Two types of error:
"""
1) SyntaxError
2) Runtime error -- Exception Error

NOTE : Exception handling concept is related to Runtime error only
"""

# What is Exception?
"""
An unwanted  and unexpected event that disturbs the normal flow of the program
"""

# Default Exception Handling
"""
Every exception in python is an object. 
For every exception type the corresponding class is available.

To prevent this abnormal termination we should handle exceptions explicitly
By using these 5 keywords : try, except, else, finally, raise
"""

# Types of Exceptions
"""
1) Predefined exceptions / Inbuilt exceptions
2) User defined exceptions / Customized exceptions
"""

# Predefined exceptions / Inbuilt exceptions
"""
Exceptions which are raised automatically by python

example1: print(10/0) --> ZeroDivisionError
example2: x = int("ten") --> ValueError
example3: print(10+"hello") --> TypeError
"""

# User defined exceptions / Customized exceptions
"""
Exceptions which are raised by user
Create your own customized exceptions using raise keyword similar like throw keyword in java
example:
# def recharge(number):
#     if number is not valid:
#         raise InvalidCouponCodeException
"""


class TooYoungException(Exception):
    def __init__(self, arg):
        self.msg = arg


class TooOldException(Exception):
    def __init__(self, arg):
        self.msg = arg


age = int(input("Enter age: "))
if age > 60:
    raise TooOldException("Not eligible")
elif age < 18:
    raise TooYoungException("Not eligible for license")
else:
    print("Thanks in else block")


# Exception Hierarchy
"""
BaseException --> Exception, SystemExit, GeneratorExit, KeyboardInterrupt etc..

Exception --> ArithmeticError, LookUpError, OSError, AttributeError, EOFError, NameError, TypeError, ValueError etc.. 

ArithmeticError --> ZeroDivisionError, FloatingPointError, OverflowError

LookUpError --> IndexError, KeyError

OSError --> FileNotFoundError, InterruptedError, TimeOutError, PermissionError
"""

# case 1:
try:
    print(10/0)
except ZeroDivisionError as e:
    print("Exception type: ", e.__class__)  # Exception type:  <class 'ZeroDivisionError'>
    print("Exception type: ", type(e))  # Exception type:  <class 'ZeroDivisionError'>
    print("Exception class name: ", e.__class__.__name__)  # Exception class name:  ZeroDivisionError


# case 2:
try:
    print(10/0)
except BaseException as e:
    print("Exception type: ", e.__class__)  # Exception type:  <class 'ZeroDivisionError'>
    print("Exception type: ", type(e))  # Exception type:  <class 'ZeroDivisionError'>
    print("Exception class name: ", e.__class__.__name__)  # Exception class name:  ZeroDivisionError


# case 3:
try:
    print(10/0)
except (ZeroDivisionError, ValueError, Exception, BaseException) as e:
    print("Exception type: ", e.__class__)  # Exception type:  <class 'ZeroDivisionError'>
    print("Exception type: ", type(e))  # Exception type:  <class 'ZeroDivisionError'>
    print("Exception class name: ", e.__class__.__name__)  # Exception class name:  ZeroDivisionError
