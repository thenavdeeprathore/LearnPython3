"""
What is List:
------------
 List is represented by --> [ ]
 List objects are MUTABLE {we can change the content of the list}
 Insertion order is preserved
 Duplicate objects are allowed
 Indexing - supports both +ve and -ve indexing
 Dynamic - we can increase the size and decrease the size
 Heterogeneous objects are allowed {Different data types together}

When to use List:
----------------
If we want to represent a group of individual objects as a single entity where,
=> insertion order is preserved and
=> duplicates objects are allowed
then we should go for List.
"""


# -------------------------------- Creation of List Objects:
'''
There are 5 different ways to create a list:
-------------------------------------------
1) Empty list l = []
2) If we know elements already then l = [10, 20, 30, 40]
3) Dynamic input using command line l = eval(input())
4) By using list() function l = list()
5) With split() Function l = str.split()
'''


# 1) Create empty list object by using []
empty_list = []
print(empty_list)  # []
print(type(empty_list))  # <class 'list'>


# 2) If we know elements already then
number_list = [10, 20, 30, 40]
print(number_list)  # [10, 20, 30, 40]
print(type(number_list))  # <class 'list'>


# 3) Dynamic input using command line -- eval(input())
commandline_list = eval(input("Enter List: "))  # [10, 20, 30, 40]
print(commandline_list)  # [10, 20, 30, 40]
print(type(commandline_list))  # <class 'list'>


# 4) By using list() function
# 4.1) empty list
empty_list_function = list()
print(empty_list_function)  # []
print(type(empty_list_function))  # <class 'list'>

# 4.2) convert string to list: {can only take one argument}
str_list = list("python")
print(str_list)  # ['p', 'y', 't', 'h', 'o', 'n']

# 4.3) list() function only takes 1 argument
# l5 = list(10, 20, 30, 40, 50)
# print(l5)   # TypeError: list() takes at most 1 argument (5 given)

# 4.4) range function
list_range = list(range(0, 10, 2))
print(list_range)  # [0, 2, 4, 6, 8]


# 5) With split() Function:
s = "Learning Python is very very easy !!!"
str_split_list = s.split()  # By default split takes whitespaces
print(str_split_list)  # ['Learning', 'Python', 'is', 'very', 'very', 'easy', '!!!']
print(type(str_split_list))  # <class 'list'>


# -------------------------------- List is Heterogeneous:
# Homogeneous list
l1 = [10, 20, 30, 40]
print(l1)
print(type(l1))


# Heterogeneous list
l2 = [10, 10.23, "Python"]
print(l2)
print(type(l2))


# -------------------------------- Accessing elements of List:
'''
1) By using index
2) By using slice operator (:)
'''
# 1) By using Index:
# List follows zero based index. ie index of first element is zero.
# List supports both +ve and -ve indexes.
# +ve index meant for Left to Right
# -ve index meant for Right to Left

list1 = [10, 20, 30, 40]
print(list1[0])  # 10
print(list1[1])  # 20
print(list1[2])  # 30
print(list1[3])  # 40
print(list1[-1])  # 40
print(list1[-2])  # 30
print(list1[-3])  # 20
print(list1[-4])  # 10
# print(list1[100])  # IndexError: list index out of range


# 2) By using Slice Operator:
# Syntax: list2 = list1[start:stop:step]
# Start  It indicates the Index where slice has to Start
# Stop  It indicates the Index where slice has to End
# Step  increment value {Default Value is 1}

# Forward Direction:
#       default value for begin: 0
#       default value for end: len(list)
# NOTE: In forward direction if end value is 0 then result is always empty

# Backward Direction:
#       default value for begin: -1
#       default value for end: (len(list)+1)
# NOTE: In backward direction if end value is -1 then result is always empty


n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(n[0:10])  # forward direction
print(n[0:len(n)])  # forward direction
print(n[-11:])  # backward direction
print(n[-(len(n)+1):])  # backward direction
print(n[2:7:2])  # [3, 5, 7] {[2:6:2]}
print(n[4::2])  # [5, 7, 9]
print(n[3:7])  # [4, 5, 6, 7]
print(n[8:2:-2])  # [9, 7, 5] {[8:3:-2]}
print(n[4:100])  # [5, 6, 7, 8, 9, 10]
print(n[1:])  # [2, 3, 4, 5, 6, 7, 8, 9, 10]
print(n[:])  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(n[:2])  # [1, 2]
print(n[1:3:2])  # [2]
print(n[-4:-2])  # [7, 8]
print(n[:-2])  # [1, 2, 3, 4, 5, 6, 7, 8]
print(n[-3:])  # [8, 9, 10]
print(n[4:0:2])  # In forward direction if end value is 0 then result is always empty
print(n[-1:-4:2])  # In backward direction if end value is -1 then result is always empty
print(n[::1])  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(n[::-1])  # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1] {Reverse list}


# -------------------------------- List vs Mutability:
'''
Once we creates a List object, we can modify its content. Hence List objects are mutable.
'''
n = [10, 20, 30, 40]
print(n)  # [10, 20, 30, 40]
n[1] = 777
print(n)  # [10, 777, 30, 40]


# -------------------------------- Traversing the Elements of List:
'''
The sequential access of each element in the list is called traversal.
1) By using while Loop:
2) By using for Loop:
'''
# 1) By using while Loop:
l = [10, 20, 30, 40]
i = 0
while i < len(l):
    print(l[i])
    i = i + 1


# 2) By using for Loop:
n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for items in n:
    print(items)


# 3) To display only Even Numbers:
n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for items in n:
    if items % 2 == 0:
        print(items)


# 4.1) To display Elements by Index wise - Way 1:
n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
i = 0
for items in n:
    print("List elements at the index {} is {}".format(i, items))
    i = i + 1

# 4.2) To display Elements by Index wise - Way 2:
n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
i = 0
while i < len(n):
    print(n[i], "is available at positive index: ", i, "and at negative index: ", i-len(n))
    i = i + 1


# -------------------------------- Mathematical operators for List:
"""
1) Concatenation operator (+)
2) Repetition operator (*)
"""

# Concat operator
# case 1 - Valid
l1 = [10, 20, 30]
l2 = [40, 50, 5]
l3 = l1 + l2
print(l3)  # [10, 20, 30, 40, 50, 5]

# case 2 - Invalid
l1 = [10, 20, 30]
# l2 = l1 + 40  # TypeError {You can concat only list to list}

# case 3 - Valid
l1 = [10, 20, 30]
l2 = l1 + [40]
print(l2)  # [10, 20, 30, 40]

# case 4 - Invalid
l1 = [10, 20, 30]
# l2 = l1 + (1, 2, 3)  # TypeError {List and Tuple concatenation is not possible}


# Repetition operator
l1 = [10, 20]
l2 = l1*2  # compulsory one arg must be list and one arg must be int
print(l2)  # [10, 20, 10, 20]

# certification exam:
l1 = [10, 20]
l2 = [30, 40]
l3 = l1 + l2
l4 = l3*3
print(l4)  # [10, 20, 30, 40, 10, 20, 30, 40, 10, 20, 30, 40]


# -------------------------------- Equality operators for List:
"""
==
The number of the elements must be same
The order of the elements must be same
The content of the elements must be same

!=
"""

l1 = ['dog', 'cat', 'rat']
l2 = ['dog', 'cat', 'rat']
l3 = ['DOG', 'CAT', 'RAT']
l4 = ['cat', 'rat', 'dog']
print(l1 == l2)  # True
print(l1 == l3)  # False
print(l1 == l4)  # False
print(l1 != l4)  # True


# -------------------------------- Relational operators for List:
"""
<
<=
>
>=
"""
# Note: content comparison only in relational operators
# First element in both list will be checked first [10] [50]
l1 = [10, 20, 30, 40]
l2 = [50, 60]
print(l1 < l2)  # True
print(l1 <= l2)  # True
print(l1 > l2)  # False
print(l1 >= l2)  # False


# -------------------------------- Special operators for List:
"""
Membership operators: {check content}
in
not in

Identity operators: {memory/address comparison}
is
is not
"""
l1 = [10, 20, 30, 40]
print(10 in l1)  # True
print(50 not in l1)  # True
print(50 in l1)  # False


# id
# in, not in    checking data available or not
# is, is not    memory comparison
# == !=         data comparison
l1 = [10, 20, 30, 40]
l2 = [10, 20, 30, 40]
l3 = l1
l4 = [10, 20, 50, 60]

print(id(l1))  # 23170440
print(id(l2))  # 23170792
print(id(l3))  # 23170440
print(id(l4))  # 23170184
print(l1 == l2)  # True
print(l1 == l3)  # True
print(l1 != l4)  # True
print(l1 is l2)  # False {Most important point}
print(l1 is l3)  # True
print(l1 is not l4)  # True
print(20 in l1)  # True
print(30 in l2)  # True
print(100 not in l1)  # True
