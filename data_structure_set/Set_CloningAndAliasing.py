"""
Aliasing of Set Objects: =
------------------------
=>  The process of giving another reference variable to the existing list is called aliasing.
=>  The problem in this approach is by using one reference variable if we are changing
    content, then those changes will be reflected to the other reference variable.

Cloning of Set Objects: copy()
------------------------
=>  To overcome aliasing problem we should go for cloning.
=>  The process of creating exactly duplicate independent object is called cloning.
=>  We can implement cloning by using copy() function.
"""

# Aliasing
s1 = {10, 20, 30, 40}
s2 = s1
print(s1)
print(s2)
s1.add(777)
print(s1)
print(s2)


# Cloning
# By using copy() function
s1 = {10, 20, 30, 40}
s2 = s1.copy()
print(s1)
print(s2)
s1.add(999)
print(s1)
print(s2)

"""
Difference between = Operator and copy() Function
    = Operator meant for aliasing
    copy() Function meant for cloning
"""
