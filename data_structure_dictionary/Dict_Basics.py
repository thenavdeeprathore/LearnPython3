"""
 We can use List, Tuple and Set to represent a group of individual objects as a single entity.
 If we want to represent a group of objects as key-value pairs then we should go for Dictionary.

=> Dictionaries are represented as d = {key:value, key:value}
=> Dictionaries are mutable
=> Dictionaries are dynamic -- we can increase the size and decrease the size
=> Heterogeneous objects are allowed for both key and values.
=> Duplicate keys are not allowed but values can be duplicated.
=> Insertion order is not preserved
=> indexing and slicing concepts are not applicable

Note: In C++ and Java Dictionaries are known as "Map" where as in Perl and Ruby it is known as "Hash"

When to use Dictionaries:
----------------
If we want to represent a group of individual objects as key-value pairs where,
=> insertion order is not preserved and
=> duplicates keys are not allowed but values can be duplicated
then we should go for Dictionaries.
"""

# -------------------------------- Creation of Dict Objects:
# empty dict -- {}
d = {}
print(d)  # {}
print(type(d))  # <class 'dict'>

# empty dict -- dict()
d = dict()
print(d)  # {}
print(type(d))  # <class 'dict'>

# If we know the data already
d = {10: "tom", 20: "jerry"}
print(d)  # {10: 'tom', 20: 'jerry'}
print(type(d))  # <class 'dict'>

# By using dict() to convert into dictionary
'''
These many combinations are valid with only 2 arguments
list of lists
list of tuples
tuple of tuples
tuple of lists
set of tuples

set of lists combination is Invalid
'''
l = [(100, 'a'), (200, 'b')]
d = dict(l)
print(d)  # {100: 'a', 200: 'b'}
print(type(d))  # <class 'dict'>

# By using dynamic input -- eval
d = eval(input("Enter a dict: "))
print(d)


# -------------------------------- Access elements from Dict:
# We can access data by using keys d[key]
d = {10: "tom", 20: "jerry", 30: "minnie"}
print(d[10])  # tom
print(d[20])  # jerry

# If the specified key is not available then we will get KeyError
# print(d[400])  # KeyError: 400

# We can prevent this by checking whether key is already available or not by using
# by using in operator
if 400 in d:
    print(d[400])
else:
    print("Key is not available")


# access directly using keys or values or items
print(d.keys())  # dict_keys([10, 20, 30])
print(d.values())  # dict_values(['tom', 'jerry', 'minnie'])
print(d.items())  # dict_items([(10, 'tom'), (20, 'jerry'), (30, 'minnie')])


# -------------------------------- Mathematical and Relation operators for List:
# Mathematical and Relational Operators are not allowed in Dict
'''
1) Concatenation operator (+)
2) Repetition operator (*)
3) Relational operator > < >= <=
'''
d1 = {100: 'tom', 200: 'jerry'}
d2 = {300: 'minnie', 400: 'noddy'}
# print(d1 + d2)  # TypeError: unsupported operand type(s) for +: 'dict' and 'dict'
# print(d1 * 3)  # TypeError: unsupported operand type(s) for *: 'dict' and 'int'
# print(d1 > d2)  # TypeError: '>' not supported between instances of 'dict' and 'dict'
# print(d1 < d2)  # TypeError: '<' not supported between instances of 'dict' and 'dict'


# -------------------------------- Equality operators for List:
d11 = {100: 'tom', 200: 'jerry'}
d12 = {100: 'tom', 200: 'jerry'}
print(d11 == d12)  # True
print(d11 != d12)  # False

# -------------------------------- Special operators for List:
"""
Membership operators: {check content}
in
not in
"""
# NOTE : membership operators will only check for keys
d = {100: 'tom', 200: 'jerry', 300: 'minnie', 400: 'noddy'}
print(100 in d)  # True
print('jerry' in d)  # False {only check for keys}
print(777 in d)  # False
print(999 not in d)  # True
