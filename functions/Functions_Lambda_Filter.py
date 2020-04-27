"""
filter() Function:
------------------
=>  We can use filter() function to filter values from the given sequence based on some condition.
=>  filter(function, sequence)
=>  Where Function Argument is responsible to perform conditional check Sequence can be
    List OR Tuple OR String
"""


# case 1: filter even numbers without lambda expressions
def is_even(x):
    if x % 2 == 0:
        return True
    else:
        return False


number_list = [0, 5, 10, 15, 20, 25, 30]
even_list = list(filter(is_even, number_list))
print(even_list)


# case 2: filter even and odd numbers with lambda expressions
number_tuple = (0, 5, 10, 15, 20, 25, 30, 35, 40)

even_tuple = tuple(filter(lambda x: x % 2 == 0, number_tuple))
print(even_tuple)  # (0, 10, 20, 30, 40)

odd_list = list(filter(lambda x: x % 2 != 0, number_tuple))
print(odd_list)  # [5, 15, 25, 35]


# divisible by 3 and odd
number_list = [0, 5, 10, 15, 20, 25, 30]
div_by_3_odd = list(filter(lambda n: n % 3 == 0 and n % 2 != 0, number_list))
print(div_by_3_odd)  # [15]
