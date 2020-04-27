"""
Dictionary:
-----------
 We can use List, Tuple and Set to represent a group of individual objects as a single entity.
 If we want to represent a group of objects as key-value pairs then we should go for Dictionary.

=> Dictionaries are represented as d = {key:value, key:value}
=> Dictionaries are mutable
=> Dictionaries are dynamic -- we can increase the size and decrease the size
=> Heterogeneous objects are allowed for both key and values.
=> Duplicate keys are not allowed but values can be duplicated.
    - dict keys must be : immutable {tuple, Number(int, float), String, Boolean etc..}
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

# ################################################ Creation of dictionary objects:
'''
There are 5 different ways to create a dictionary:
-------------------------------------------------
1) Empty dict d = {}
2) Empty dict d = dict()
3) If we know elements already then d = {10: "tom", 20: "jerry"}
4) By using dict() function d = dict() to convert into dictionary
        - list of lists
        - list of tuples
        - tuple of tuples
        - tuple of lists
        - set of tuples
5) Dynamic input using command line l = eval(input())
'''
# empty dict -- {}
d = {}
print(d)  # {}
print(type(d))  # <class 'dict'>

# empty dict -- dict()
d = dict()
print(d)  # {}
print(type(d))  # <class 'dict'>

# If we know the elements already
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

# ################################################ Dictionary key types:
# dict keys must be : immutable {tuple, Number(int, float), String etc}
# dict values can be of any type

# d = {[1, 2]: "John", 22: 20, 33: "Chris"}  # TypeError: un hashable type: 'list'

d = {(1, 2): "python", 3: "java"}
print(d)  # {(1, 2): 'python', 3: 'java'}
print(d[(1, 2)])  # python

d = {None: None}
print(d)  # {None: None}

# ################################################ Dictionary key duplicate:
# Duplicate keys are not allowed, it will overwrite the existing one
d = {111: "tom", 111: "jerry"}
print(d)  # {111: 'jerry'}

# Duplicate values are allowed
d = {111: "tom", 222: "tom"}
print(d)  # {111: "tom", 222: "tom"}

# ################################################ Dictionary is heterogeneous:
# Homogeneous key and value dictionary
d = {1: "a", 2: "b"}

# Heterogeneous key dictionary
d = {1: "number", "a": "string", (10, 20): "tuple"}
print(d)  # {1: 'number', 'a': 'string', (10, 20): 'tuple'}

# Heterogeneous value dictionary
d = {"number": 1, "string": "a", "tuple": (10, 20)}
print(d)  # {'number': 1, 'string': 'a', 'tuple': (10, 20)}

# ################################################ Accessing elements of dictionary:
# We can access data by using keys d[key]
d = {10: "tom", 20: "jerry", 30: "minnie"}
print(d[10])  # tom
print(d[20])  # jerry

# If the specified key is not available then we will get KeyError
# print(d[400])  # KeyError: 400

# We can prevent the error by checking whether key is already available or not by using 2 ways:
# 1) By using in operator
if 400 in d:
    print(d[400])
else:
    print("Key is not available")

# 2) By using get() function
print(d.get(400))  # None

# Access directly using keys or values or items
print(d.keys())  # dict_keys([10, 20, 30])
print(d.values())  # dict_values(['tom', 'jerry', 'minnie'])
print(d.items())  # dict_items([(10, 'tom'), (20, 'jerry'), (30, 'minnie')])

# ################################################ Dictionary vs Mutability:
# Keys must be unique
d = {10: "tom", 20: "jerry", 10: "minnie"}
print(d)  # {10: 'minnie', 20: 'jerry'}

# Values can be duplicate
d = {10: "vicky", 20: "vicky", 30: "vicky"}
print(d)  # {10: 'vicky', 20: 'vicky', 30: 'vicky'}

# ################################################ Traversing the Elements of dictionary:
'''
The sequential access of each element in the dictionary is called traversal.
1) By using for Loop:
'''
d = {10: "tom", 20: "jerry", 30: "minnie"}

# for loop with only key arg
for x in d:
    print(x, d[x])
# 10 tom
# 20 jerry
# 30 minnie

# for loop with both key, value args
for k, v in d.items():
    print(k, "-->", v)
# 10 --> tom
# 20 --> jerry
# 30 --> minnie

# ################################################ Operators for dictionary:
'''
1) Mathematical 02_operators {dict doesn't support}
        Concatenation operator (+)
        Repetition operator (*)
2) Relation 02_operators {dict doesn't support}
        <
        <=
        >
        >=
3) Equality 02_operators
        ==
        !=
4) Membership 02_operators: {check content}
        in
        not in
        # NOTE : membership 02_operators will only check for keys
5) Identity 02_operators: {memory/address comparison}
        is
        is not
'''

dict1 = {111: "IronMan", 222: "BatMan"}
dict2 = {333: "Hulk", 444: "Thor"}
dict3 = dict1

# Dictionary doesn't supports Mathematical 02_operators
# print(dict1 + dict2)  # TypeError: unsupported operand type(s) for +: 'dict' and 'dict'
# print(dict1 * 3)  # TypeError: unsupported operand type(s) for *: 'dict' and 'int'

# Dictionary doesn't supports Relational 02_operators
# print(dict1 < dict2)  # TypeError: '<' not supported between instances of 'dict' and 'dict'
# print(dict1 > dict2)  # TypeError: '>' not supported between instances of 'dict' and 'dict'

print(dict1 == dict2)  # False
print(dict1 == dict3)  # True
print(dict1 != dict2)  # True

print(111 in dict1)  # True
print(12 in dict1)  # False
print(13 not in dict1)  # True
# NOTE : membership 02_operators will only check for keys, for values it will always give False
print("Thor" in dict2)  # False

# id of dict1 and dict3 are same
print(id(dict1))
print(id(dict2))
print(id(dict3))

print(dict1 is dict2)  # False
print(dict1 is dict3)  # True
print(dict1 is not dict2)  # True

# ##############################  type casting ##############################
print(list(d.keys()))  # [1, 4, 2, 3]
print(list(d.values()))  # ['aa', 'bb', 'cc', 'dd']
print(list(d.items()))  # [(1, 'aa'), (4, 'bb'), (2, 'cc'), (3, 'dd')]

print(tuple(d.keys()))  # (1, 4, 2, 3)
print(set(d.keys()))  # {1, 2, 3, 4}
