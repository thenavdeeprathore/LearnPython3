"""
reduce() Function:
-----------------
=>  reduce() function reduces sequence of elements into a single element by applying the specified function.
=>  reduce(function,sequence)
=>  reduce() function present in functools module and hence we should write import statement.

filter vs map vs reduce:
------------------------
Filter      : Input = 10    Output <= 10
Map         : Input = 10    Output = 10
Reduce      : Input = 10    Output = 1
"""
from functools import reduce

l = [10, 20, 30, 40]

add_list = reduce(lambda x, y: x + y, l)
print(add_list)  # 100

mul_list = reduce(lambda x, y: x * y, l)
print(mul_list)  # 240000

add_100_numbers = reduce(lambda x, y: x + y, range(1, 101))
print(add_100_numbers)  # 5050

# NOTE: reduce is not a python inbuilt function, compulsory we must import functools
