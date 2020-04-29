"""
Special Operators:
---------------------
Python defines the following 2 special operators
1) Identity Operators {is, is not}
2) Membership operators {in, not in}

1) Identity Operators
--------------------
=>  We can use identity operators for address comparison.
=>  There are 2 identity operators are available
1) is
2) is not
=>  r1 is r2 returns True if both r1 and r2 are pointing to the same object.
=>  r1 is not r2 returns True if both r1 and r2 are not pointing to the same object.

Note: We can use is operator for address comparison where as == operator for content comparison.

2) Membership Operators:
----------------------
=>  We can use Membership operators to check whether the given object present in the
    given collection. (It may be String, List, Set, Tuple OR Dict)
=>  In  Returns True if the given object present in the specified Collection
=>  not in  Returns True if the given object not present in the specified Collection
"""
# ########## Identity operators
# case 1:
a = 10
b = 10
print(a is b)  # True
x = True
y = True
print(x is y)  # True
print(x is not y)  # False
i = "python"
j = "python"
print(id(i))  # 47232736
print(id(j))  # 47232736
print(i is j)  # True

# case 2:
list1 = ["one", "two", "three"]
list2 = ["one", "two", "three"]
print(id(list1))  # 28700360
print(id(list2))  # 28870472
print(list1 is list2)  # False
print(list1 is not list2)  # True
print(list1 == list2)  # True

# ########## Membership operators
# case 1:
x = "hello learning Python is very easy!!!"
print('h' in x)  # True
print('d' in x)  # False
print('d' not in x)  # True
print('Python' in x)  # True

# case 2:
list1 = ['tom', 'jerry', 'micky']
print('jerry' in list1)  # True
print('vicky' in list1)  # False
print('vicky' not in list1)  # True
