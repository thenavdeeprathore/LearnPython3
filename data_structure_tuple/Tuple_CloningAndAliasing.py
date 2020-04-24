"""
Aliasing of Tuple Objects: =
------------------------
=>  The process of giving another reference variable to the existing tuple is called aliasing.
=>  The problem in this approach is by using one reference variable if we are changing
    content, then those changes will be reflected to the other reference variable.

Cloning of Tuple Objects: [:] or [::]
------------------------
=>  To overcome aliasing problem we should go for cloning.
=>  The process of creating exactly duplicate independent object is called cloning.
=>  AttributeError: 'tuple' object has no attribute 'copy'
"""

# Aliasing
t1 = (10, 20, 30, 40)
t2 = t1
print(t1)  # (10, 20, 30, 40)
print(t2)  # (10, 20, 30, 40)

# Cloning
# By using slicing [:] or [::]
t1 = (10, 20, 30, 40)
t2 = t1[:]
print(t1)  # (10, 20, 30, 40)
print(t2)  # (10, 20, 30, 40)

# Note: In practical we don't use this aliasing and cloning much due to Tuple immutability
