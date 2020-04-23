"""
Aliasing of List Objects: =
------------------------
=>  The process of giving another reference variable to the existing list is called aliasing.
=>  The problem in this approach is by using one reference variable if we are changing
    content, then those changes will be reflected to the other reference variable.

Cloning of List Objects: [:] or [::] or copy()
------------------------
=>  To overcome aliasing problem we should go for cloning.
=>  The process of creating exactly duplicate independent object is called cloning.
=>  We can implement cloning by using slice operator or by using copy() function.
"""

# Aliasing
l1 = [10, 20, 30, 40]
l2 = l1
l1.append(50)
print(l1)  # [10, 20, 30, 40, 50]
print(l2)  # [10, 20, 30, 40, 50]
l2.remove(20)
l2.pop()
print(l1)  # [10, 30, 40]
print(l2)  # [10, 30, 40]

# Cloning
# By using slicing [:] or [::]
l1 = [10, 20, 30, 40]
l2 = l1[:]
print(l1)  # [10, 20, 30, 40]
print(l2)  # [10, 20, 30, 40]
l1[1] = 999
print(l1)  # [10, 999, 30, 40]
print(l2)  # [10, 20, 30, 40]

# Bu using copy() method
l1 = [10, 20, 30, 40]
l2 = l1.copy()
print(l1)  # [10, 20, 30, 40]
print(l2)  # [10, 20, 30, 40]
l1[2] = 1579
print(l1)  # [10, 20, 1579, 40]
print(l2)  # [10, 20, 30, 40]


"""
Difference between = Operator and copy() Function
    = Operator meant for aliasing
    copy() Function meant for cloning
"""
