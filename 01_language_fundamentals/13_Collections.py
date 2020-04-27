# Collections

"""
# A group of objects represented as a single entity is called Collections:

list
tuple
set
frozenset
dictionary
range
bytes
bytearray
"""


# list
"""
1) []
2) Heterogeneous objects are allowed {different data types}
3) Order is preserved
4) Duplicates are allowed
5) Indexing and Slicing
6) Growable in nature
7) Mutable --> can change
"""

# tuple
"""
()

Exactly same as list except tuple is Immutable.

Read only version of list is Tuple
"""

# set
"""
{}

Mutable -- can change

List vs Set:
-------------
1) In set, Duplicates are not allowed
2) In set, Order is not preserved
"""

# frozenset
"""
1) It is exactly same as set except that it is immutable.
2) Hence we cannot use add or remove functions.

tuple vs frozenset:
-------------------
1) In frozenset, order is not preserved
2) In frozenset, duplicates are not allowed
3) In frozenset, indexing and slicing are not allowed
"""

# dict
"""
If we want to represent a group of values as key-value pairs then we should go for dict data type.

Eg: d = {101:'tom',102:'jerry',103:'john'}

Duplicate keys are not allowed but values can be duplicated.

If we are trying to insert an entry with duplicate key then old value will be replaced with new value

Note: Dict is Mutable
List vs Dict:
-------------
1) In Dict, Order is not preserved
2) In Dict, indexing and slicing are not allowed
"""

# range
"""
range Data Type represents a sequence of numbers.

The elements present in range Data type are not modifiable. i.e range Data type is
immutable.
"""
r = range(10)
print(r)  # range(0, 10)
print(type(r))  # <class 'range'>


for i in r:
    print(i)

# 0 to 9


# Mutable vs Immutable
"""
bytearray
list
set
dict

These are the only mutable data types
"""