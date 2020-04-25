# packing
a = 10
b = 20
c = 30
set_packing = {a, b, c}
print(set_packing)  # {10, 20, 30}
print(type(set_packing))  # <class 'set'>

# unpacking
set_unpacking = {10, 11.22, "Python", True}
a, b, c, d = set_unpacking
print(a)  # 10
print(type(a))  # <class 'int'>
print(b)  # 11.22
print(type(b))  # <class 'float'>
print(c)  # Python
print(type(c))  # <class 'str'>
print(d)  # True
print(type(d))  # <class 'bool'>

"""
# Note: Unpack all the values
-----------------------------
At the time of set unpacking the number of variables and number of values
should be same, otherwise we will get ValueError.

Eg:
s = {10, 20, 30, 40}
a, b, c = s  ValueError: too many values to unpack (expected 3)
"""