"""
Recursive Functions
-------------------
A function that calls itself is known as Recursive Function.

The main advantages of recursive 07_functions are:
1) We can reduce length of the code and improves readability.
2) We can solve complex problems very easily.
"""


# Factorial without Recursion
def factorial(n):
    result = 1
    while n >= 1:
        result = result * n
        n = n - 1
    return result


print(factorial(3))  # 6
print(factorial(4))  # 24


# Factorial with Recursion
def factorial(n):
    if n == 0:
        result = 1
    else:
        result = n * factorial(n-1)
    return result


for i in range(11):
    print(f'The factorial of {i} is {factorial(i)}')
# The factorial of 0 is 1
# The factorial of 1 is 1
# The factorial of 2 is 2
# The factorial of 3 is 6
# The factorial of 4 is 24
# The factorial of 5 is 120
# The factorial of 6 is 720
# The factorial of 7 is 5040
# The factorial of 8 is 40320
# The factorial of 9 is 362880
# The factorial of 10 is 3628800


# Factorial with Recursion tracing
# factorial(n) = n * factorial(n-1)
def factorial(n):
    print(f'Execution of factorial for n {n}')
    if n == 0:
        result = 1
    else:
        result = n * factorial(n-1)
    print(f'Returning result of factorial ({n}) is {result}')
    return result


print(factorial(3))


# Maximum recursion depth in python
# 995 times as per 3.6 version
count = 0


def factorial(n):
    global count
    count = count + 1
    print(f'Execution of factorial for n {n}')
    if n == 0:
        result = 1
    else:
        result = n * factorial(n-1)
    return result


print(factorial(995))
print("The number of times factorial function execution: ", count)  # 996
# print(factorial(996))  # RecursionError: maximum recursion depth exceeded while calling a Python object
