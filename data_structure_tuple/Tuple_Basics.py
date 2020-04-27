"""
What is Tuple:
------------
Tuple is same as list except it is Immutable and non-dynamic {Not grow-able}

 Tuple is represented by --> ( )
 Tuple objects are IMMUTABLE {we cannot perform any changes in the tuple}
   Hence Tuple is Read only version of List
 Insertion order is preserved
 Duplicate objects are allowed
 Indexing - supports both +ve and -ve indexing
 Heterogeneous objects are allowed {Different data types together}

Note:
We have to take special care about single valued tuple.
Compulsory the value should ends with comma, otherwise it is not treated as tuple.

() Parenthesis are optional but recommended to use.

When to use Tuple:
----------------
If our data is fixed and never changes then we should go for Tuple.
"""

# -------------------------------- Creation of Tuple Objects:
"""
1) empty tuple
    t = ()
2) single valued tuple
    t = (10,)
    t = 10,
3) Multi valued tuple
    t = (10, 20, 30)
    t = 10, 20, 30
    t = (10, 20, 30,)
    t = 10, 20, 30,
4) By using tuple() Function:
    t = tuple(any sequence)
5) Dynamic input using command line
    t = eval(input())
"""

# EMPTY TUPLE
t = ()
print(t)  # ()
print(type(t))  # <class 'tuple'>


# SINGLE VALUED TUPLE
# case 1: Compulsory the value should ends with comma to be represented as a tuple
t = (10,)
print(t)  # (10,)
print(type(t))  # <class 'tuple'>

# case 2: Invalid, This is not a tuple if we use only single value without a comma at the end
t = (10)
print(t)  # 10
print(type(t))  # <class 'int'>


# MULTI VALUED TUPLE
# case 1: Best practise within () parenthesis
t = (1, 2, 3, 4, 5)
print(t)  # (1, 2, 3, 4, 5)
print(type(t))  # <class 'tuple'>

# case 2: () parenthesis is optional --> Valid but not a good practise
t = 10, 20, 30, 40
print(t)  # (10, 20, 30, 40)
print(type(t))  # <class 'tuple'>

# case 3: adding comma (,) at the end of the tuple with () parenthesis
t = (1, 2, 3, 4, 5,)
print(t)  # (1, 2, 3, 4, 5)
print(type(t))  # <class 'tuple'>

# case 4: adding comma , at the end of the tuple without () parenthesis
t = 1, 2, 3, 4, 5,
print(t)  # (1, 2, 3, 4, 5)
print(type(t))  # <class 'tuple'>


# BY USING tuple() FUNCTION:
# case 1: By using list
l = [10, 20, 30]
t = tuple(l)
print(t)  # (10, 20, 30)
print(type(t))  # <class 'tuple'>

# case 2: By using range()
t = tuple(range(1, 11))
print(t)  # (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

# case 3: any str
t = tuple("hello")
print(t)  # ('h', 'e', 'l', 'l', 'o')


# DYNAMIC INPUT USING COMMAND LINE -- eval()
t = eval(input("Enter a tuple: "))
print(t)


# -------------------------------- Accessing elements of Tuple:
'''
1) By using index
2) By using slice operator (:)
'''
# 1) By using Index:
t = (10, 20, 30, 40)
print(t[0])  # 10
print(t[-1])  # 40
# print(t[100])  # IndexError: tuple index out of range

# 2) By using Slice Operator:
t = (100, 200, 300, 400, 500)
print(t[1:5])  # (200, 300, 400, 500)
print(t[2:100])  # (300, 400, 500)
print(t[::2])  # (100, 300, 500)


# -------------------------------- Tuple vs Mutability:
'''
Once we creates tuple, we cannot change its content.
Hence tuple objects are immutable.
'''
t = (100, 200, 300)
# t[1] = 400  # TypeError: 'tuple' object does not support item assignment


# -------------------------------- Tuple is Heterogeneous:
t = (10, 20, "tom", "jerry", True)
print(t)


# -------------------------------- Tuple is Duplicate:
t = (100, 200, 300, 100, 200, 100)
print(t)


# -------------------------------- Traversing the Elements of Tuple:
'''
The sequential access of each element in the tuple is called traversal.
1) By using while Loop:
2) By using for Loop:
'''
# 1) By using while Loop:
t = (10, 20, 30, 40)
i = 0
while i < len(t):
    print(t[i])
    i = i + 1


# 2) By using for Loop:
t = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
for items in t:
    print(items)


# -------------------------------- Mathematical 02_operators for List:
"""
1) Concatenation operator (+)
2) Repetition operator (*)
"""
# case 1
t1 = (10, 20, 30)
t2 = (40, 50)
t3 = t1 + t2
print(t3)  # (10, 20, 30, 40, 50)

# case 2
# t3 = t1 + 10  # TypeError: can only concatenate tuple (not "int") to tuple
# t3 = t1 + [1, 2, 3]  # TypeError: can only concatenate tuple (not "list") to tuple

# case 3
t1 = (10, 20, 30)
t2 = t1*3
print(t2)  # (10, 20, 30, 10, 20, 30, 10, 20, 30)


# -------------------------------- Equality 02_operators for Tuple:
"""
==
The number of the elements must be same
The order of the elements must be same
The content of the elements must be same

!=
"""

t1 = ('dog', 'cat', 'rat')
t2 = ('dog', 'cat', 'rat')
t3 = ('DOG', 'CAT', 'RAT')
t4 = ('cat', 'rat', 'dog')
print(t1 == t2)  # True
print(t1 == t3)  # False
print(t1 == t4)  # False
print(t1 != t4)  # True


# -------------------------------- Relational 02_operators for Tuple:
"""
<
<=
>
>=
"""
# Note: content comparison only in relational 02_operators
# First element in both tuple will be checked first [10] [50]
t1 = [10, 20, 30, 40]
t2 = [50, 60]
print(t1 < t2)  # True
print(t1 <= t2)  # True
print(t1 > t2)  # False
print(t1 >= t2)  # False


# -------------------------------- Special 02_operators for Tuple:
"""
Membership 02_operators: {check content}
in
not in

Identity 02_operators: {memory/address comparison}
is
is not
"""
t1 = [10, 20, 30, 40]
print(10 in t1)  # True
print(50 not in t1)  # True
print(50 in t1)  # False


# id
# in, not in    checking data available or not
# is, is not    memory comparison
# == !=         data comparison
t1 = [10, 20, 30, 40]
t2 = [10, 20, 30, 40]
t3 = t1
t4 = [10, 20, 50, 60]

print(id(t1))  # 55676232
print(id(t2))  # 55676264
print(id(t3))  # 55676232
print(id(t4))  # 55676200
print(t1 == t2)  # True
print(t1 == t3)  # True
print(t1 != t4)  # True
print(t1 is t2)  # False {Most important point}
print(t1 is t3)  # True
print(t1 is not t4)  # True
print(20 in t1)  # True
print(30 in t2)  # True
print(100 not in t1)  # True
