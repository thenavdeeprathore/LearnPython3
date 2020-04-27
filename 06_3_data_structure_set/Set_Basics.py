"""
What is Set:
------------
If we want to represent a group of unique values as a single entity then we should go for set

 Set is represented by --> { }
 Set objects are MUTABLE {we can perform changes in the set}
 Heterogeneous objects are allowed {Different data types together}
 Dynamic {grow-able in nature}
 We can apply mathematical operations like union, intersection, difference.. etc on set objects

Difference between List vs Set:
------------------------------
In Set comparison to list,
- Duplicates are not allowed
- Insertion order is not preserved
- Indexing and slicing is not applicable
"""

# -------------------------------- Creation of Set Objects:
'''
1) empty set    : s = set()
2) If we have data already  : s = {10, 20, 30}
3) By using set() function
'''
# case 1: create empty set
# While creating empty set we have to take special care.
# Compulsory we should use set() function.
# s = {}  It is treated as dictionary but not empty set.
s = {}
print(s)  # {}
print(type(s))  # <class 'dict'>

s = set()
print(s)  # set()
print(type(s))  # <class 'set'>

# case 2: data is already present
s = {10, 20, 30, 40}
print(s)  # {40, 10, 20, 30}
print(type(s))  # <class 'set'>

# case 3: convert list into set
n = [1, 2, 3]
print(n)
s = set(n)
print(s)

# case 4: use range
s = set(range(1, 11, 2))
print(s)

# case 5: string into list
s = set("python")
print(s)  # {'o', 'y', 'h', 't', 'p', 'n'}

# case 6: command line input eval
s = eval(input("Enter a set value: "))
print(s)


# -------------------------------- Mathematical 02_operators for Set:
"""
Not applicable
We can't use Concatenation operator (+) and Repetition operator (*) 02_operators in set
We will get TypeError
"""
s1 = {10, 20, 30}
s2 = {40, 50, 60, 70}
# print(s1 + s2)  # TypeError: unsupported operand type(s) for +: 'set' and 'set'

# -------------------------------- Equality 02_operators for Set:
"""
Not applicable
since insertion order is not preserved, it's not possible to use == or != operator
"""
s1 = {20, 10, 30, 50}
s2 = {20, 10, 30, 50}
print(s1 == s2)  # True
print(s1 != s2)  # False

# -------------------------------- Relational 02_operators for Set:
"""
Not applicable
since insertion order is not preserved, we will get False in every relational case
"""
s1 = {20, 10, 30}
s2 = {10, 20, 30}
print(s1 < s2)  # False
print(s1 > s2)  # False


# -------------------------------- Special 02_operators for Tuple:
"""
Yes we can apply this operator in set

Membership 02_operators: {check content}
in
not in

Identity 02_operators: {memory/address comparison}
is
is not
"""
s = {10, 30, 50, 40, 20}
print(10 in s)  # True
print(40 in s)  # True
print(100 not in s)  # True
print(200 in s)  # False


# -------------------------------- summary of set creation
# Heterogeneous
s1 = {10, 20, 30, "tom", "jerry"}
print(s1)
print(type(s1))

# No duplicates
s2 = {10, 20, 30, 20, 30}
print(s2)  # {10, 20, 30}  - No duplicate is allowed

# empty {} this is dict not set
s3 = {}  # don't declare empty set like this
print(s3)
print(type(s3))  # <class 'dict'>

# empty set
s4 = set()  # empty set
print(s4)
print(type(s4))

# Immutable data can be stored in set
s5 = {10, "tom", (1, 2)}
# Immutable - int, str, tuple
print(s5)

# Mutable data can NOT be stored in set
# s6 = {[1, 2]}   # TypeError: un hashable type: 'list'
# print(s6)

# Nested Set is not allowed
# s7 = {{10, 20}, {30, 40}}   # TypeError: un hashable type: 'set'
# print(s7)
