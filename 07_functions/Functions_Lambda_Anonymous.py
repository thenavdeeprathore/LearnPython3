"""
Anonymous Functions / Lambda Functions:
-------------------
=>  Sometimes we can declare a function without any name, such type of nameless 07_functions are called
    anonymous 07_functions or lambda 07_functions.
=>  The main purpose of lambda function is just for instant use (i.e for one time usage)

Lambda Function:
----------------
=>  We can define by using lambda keyword lambda n:n*n
=>  Syntax of lambda Function: lambda argument_list : expression
=>  Note: By using Lambda Functions we can write very concise code so that readability of
    the program will be improved.
"""

# Anonymous / lambda function
s = lambda n: n * n
print(f"Square of number {4} is {s(4)}")  # Square of number 4 is 16
print(f"Square of number {5} is {s(5)}")  # Square of number 5 is 25

# Write a lambda function to find sum of two numbers
add = lambda a, b: a + b
print(f"The sum of {2} and {3} is: {add(2, 3)}")  # The sum of 2 and 3 is: 5
print(f"The sum of {5} and {7} is: {add(5, 7)}")  # The sum of 5 and 7 is: 12

# Find the greatest of 2 numbers
largest = lambda a, b: a if a > b else b
print(f"The largest of {10} and {20} number is: {largest(10, 20)}")  # The largest of 10 and 20 number is: 20
print(f"The largest of {30} and {20} number is: {largest(30, 20)}")  # The largest of 30 and 20 number is: 30

# Find the greatest of 3 numbers
largest = lambda a, b, c: a if a > b and a > c else b if b > c else c
print(f"The largest of {10} , {20} , {30} number is: {largest(10, 20, 30)}")
# The largest of 10 , 20 , 30 number is: 30

'''
Note:   Lambda Function internally returns expression value and we are not required to
        write return statement explicitly.

Note:   Sometimes we can pass function as argument to another function. In such cases
        lambda 07_functions are best choice.

# Function as argument to another function
We can use lambda 07_functions very commonly with filter(), map() and reduce() 07_functions,
because these 07_functions expect function as argument.
        filter(function, sequence)
        map(function, sequence)
        reduce(function, sequence)
'''
