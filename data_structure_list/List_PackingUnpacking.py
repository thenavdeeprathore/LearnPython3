# packing
a = 10
b = 20
c = 30
list_packing = [a, b, c]
print(list_packing)  # [10, 20, 30]
print(type(list_packing))  # <class 'list'>

# unpacking
list_unpacking = [10, 11.22, "Python", True]
a, b, c, d = list_unpacking
print(a)  # 10
print(type(a))  # <class 'int'>
print(b)  # 11.22
print(type(b))  # <class 'float'>
print(c)  # Python
print(type(c))  # <class 'str'>
print(d)  # True
print(type(d))  # <class 'bool'>

# unpacking special case:
list_unpacking = [10, 11.22, "Python", True]
a, *b = list_unpacking
print(a)  # 10
print(b)  # [11.22, 'Python', True]
print(type(b))  # <class 'list'>


"""
# Note: Unpack all the values
-----------------------------
At the time of list unpacking the number of variables and number of values
should be same, otherwise we will get ValueError.

Eg:
l = [10, 20, 30, 40]
a, b, c = t  ValueError: too many values to unpack (expected 3)
"""
