"""
Python functions:
----------------
A group of statements are repeatedly required for code re-usability
Indentation is important for the code inside the function

Any functions defined inside class are called METHODS
Any function defined outside class by their own are called FUNCTIONS

Types of functions:
------------------
1) Built in/Predefined functions
The functions which are coming along with Python software automatically, are called built in functions
        id()
        type()
        input()
        eval()
        etc..

2) User-defined functions
The functions which are developed by programmer explicitly according to business requirements
Syntax to Create User defined Functions:

def function_name(parameters):
    '''doc string'''
    -----
    -----
    return value

Note: While creating functions we can use 2 keywords
1) def (mandatory)
2) return (optional)

Biggest advantage of Python function compared to other programming language is:
------------------------------------------------------------------------------
It can return multiple values --> return x, y, z
"""


# ###################### User-defined functions ######################
# case 1: No error if there is no return type or return value in a function
def greeting():
    """ greeting function without a return type """
    print("hello, good morning")


greeting()  # hello, good morning
greeting()  # hello, good morning
greeting()  # hello, good morning
# Note: If we are not writing return statement then default return value is None
print(greeting())  # None


# case 2: Function can return multiple values
def calculator(a, b):
    """ calculator function with multiple return values """
    addition = a + b
    subtraction = a - b
    multiplication = a * b
    division = a / b
    # group of comma separated values is represent as tuple
    return addition, subtraction, multiplication, division
    # return addition  # This return code is unreachable


n1, n2, n3, n4 = calculator(5, 2)
print("The Addition is:", n1)  # The Addition is: 7
print("The Subtraction is:", n2)  # The Subtraction is: 3
print("The Multiplication is:", n3)  # The Multiplication is: 10
print("The Division is:", n4)  # The Division is: 2.5

print(calculator(5, 2))  # (7, 3, 10, 2.5)

tup = calculator(5, 2)
print("The results are: ")
for x in tup:
    print(x)
# 7
# 3
# 10
# 2.5


# ###################### Parameters to the functions ######################
"""
Parameters are inputs to the function. If a function contains parameters then at the time of calling, 
compulsory we should provide values otherwise we will get error.
"""


# case 1: function with a parameter
def greeting(name):
    """ greeting function without a return type but with a parameter """
    print(f"hello {name}, good morning")


greeting("vicky")  # hello vicky, good morning
greeting("rocky")  # hello rocky, good morning
# greeting()  # TypeError: greeting() missing 1 required positional argument: 'name'
print(greeting("vicky"))  # None


# case 2: find square of a given number
def square_number(num):
    """ square number function """
    sq = num*num
    print(f"The square of {num} is {sq}")


square_number(2)  # The square of 2 is 4
square_number(3)  # The square of 3 is 9
square_number(4)  # The square of 4 is 16


# case 3: find even and odd number
def even_odd(num):
    """ even and odd number function """
    if num % 2 == 0:
        print(f"{num} is even")
    else:
        print(f"{num} is odd")


even_odd(10)  # 10 is even
even_odd(15)  # 15 is odd
