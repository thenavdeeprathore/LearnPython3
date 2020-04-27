"""
Important Functions of Tuple:
---------------------------

I. To get Information about Tuple:
    1) len          : Returns the number of elements present in the tuple
    2) count        : Returns the number of occurrences of specified item in the tuple
    3) index        : Returns the index of first occurrence of the specified item

II. Ordering Elements of Tuple:
    4) reversed    : To reverse order of elements of any data types by creating a new object
    5) sorted      : To sort order of elements of any data types by creating a new object
"""

# I. To get Information about Tuple:

# len()
x = (10, 20, 30, 40, 50, 10, 20, 10)
print(len(x))  # 8

# count()
print(x.count(10))  # 3
print(x.count(90))  # 0

# index()
# Note: If the specified element not present in the tuple then we will get ValueError.
# print(x.index(100))  # ValueError: 100 is not in tuple
print(x.index(10))  # 0
print(x.index(50))  # 4

# Another way of doing index search is:
# tuple_name.index(element, start, end)
# start (Optional) - The position from where the search begins. {index}
# end (Optional) - The position from where the search ends. {len(tuple_name)}
print(x.index(10, 2, 6))  # 5


# II. Ordering Elements of Tuple:

# reversed()
# Note: we can't reversed using the same object, we must create a new object to reverse a tuple
t = (40, 10, 50, 30, 20)
r = reversed(t)
t1 = tuple(r)
print(t)  # (40, 10, 50, 30, 20)
print(t1)  # (20, 30, 50, 10, 40)

# sorted()
# Note: we can't sorted using the same object, we must create a new object to sort a tuple
# Ascending order
t = (40, 10, 50, 30, 20)
s = sorted(t)
t1 = tuple(s)
print(t)  # (40, 10, 50, 30, 20)
print(t1)  # (10, 20, 30, 40, 50)

# Descending order
t = (40, 10, 50, 30, 20)
s = sorted(t, reverse=True)
t1 = tuple(s)
print(t)  # (40, 10, 50, 30, 20)
print(t1)  # (50, 40, 30, 20, 10)
