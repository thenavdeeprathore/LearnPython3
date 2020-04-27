"""
map() Function:
---------------
=>  For every element present in the given sequence, apply some functionality and
    generate new element with the required modification. For this requirement we
    should go for map() function.
=>  Eg: For every element present in the list perform double and generate new list of doubles.
=>  Syntax: map(function, sequence)
=>  The function can be applied on each element of sequence and generates new sequence
"""


# case 1: map the list item double without lambda expressions
def double(x):
    return 2 * x


l = [0, 5, 10, 15, 20, 25, 30]
l1 = list(map(double, l))
print(l1)  # [0, 10, 20, 30, 40, 50, 60]


# case 2: map the list item with lambda expressions
l = [0, 5, 10, 15, 20, 25, 30]

double_list = list(map(lambda x: 2 * x, l))
print(double_list)  # [0, 10, 20, 30, 40, 50, 60]


# case 3: different sequence types
square_tuple = tuple(map(lambda x: x * x, l))
print(square_tuple)  # (0, 25, 100, 225, 400, 625, 900)


# case 4: use multiple sequence arg in map
l1 = [1, 2, 3]
l2 = [10, 20, 30]
l3 = [100, 200, 300]

print(list(map(lambda x, y: x + y, l1, l2)))  # [11, 22, 33]
print(list(map(lambda x, y, z: x + y + z, l1, l2, l3)))  # [111, 222, 333]


# case 5: extra numbers will be ignored
l1 = [1, 2, 3, 4, 5, 6, 7]
l2 = [10, 20, 30]

print(list(map(lambda x, y: x + y, l1, l2)))  # [11, 22, 33]

# We can apply map() function on multiple lists also but make sure all list should have same length.
