# All fundamental data types are Immutable {Can't change}

# Mutable -- Changeable
# Immutable -- Non changeable
"""
Fundamental Data Types vs Immutability:
--------------------------------------
=> All Fundamental Data types are immutable. i.e once we creates an object, we cannot
perform any changes in that object. If we are trying to change then with those changes
a new object will be created. This non-changeable behaviour is called immutability.

=> In Python if a new object is required, then PVM won’t create object immediately. First
it will check is any object available with the required content or not. If available then
existing object will be reused. If it is not available then only a new object will be
created. The advantage of this approach is memory utilization and performance will be
improved.

=> But the problem in this approach is, several references pointing to the same object, by
using one reference if we are allowed to change the content in the existing object then
the remaining references will be effected. To prevent this immutability concept is
required. According to this once creates an object we are not allowed to change
content. If we are trying to change with those changes a new object will be created
"""
a = 10
b = 10
print(a is b)  # True
print(id(a))  # 1626208320
print(id(b))  # 1626208320


# Mutable -- List
l1 = [10, 20, 30]
l2 = l1
print(id(l1))  # 29947336
print(id(l2))  # 29947336
l1[0] = 100
print(l1)  # [100, 20, 30]
print(l2)  # [100, 20, 30]
l2[1] = 200
print(l1)  # [100, 200, 30]
print(l2)  # [100, 200, 30]


