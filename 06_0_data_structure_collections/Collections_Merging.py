# list merging --> 2 ways
l1 = [10, 20, 30]
l2 = [40, 50, 60]
print(l1 + l2)  # [10, 20, 30, 40, 50, 60]
print([*l1, *l2])  # [10, 20, 30, 40, 50, 60]

# tuple merging --> 2 ways
t1 = (10, 20, 30)
t2 = (40, 50, 60)
print(t1 + t2)  # (10, 20, 30, 40, 50, 60)
print((*t1, *t2))  # (10, 20, 30, 40, 50, 60)

# set merging --> only 1 way
s1 = {10, 20, 30}
s2 = {40, 50, 60}
# print(s1 + s2)  # TypeError: unsupported operand type(s) for +: 'set' and 'set'
# Note: order is not preserved
print({*s1, *s2})  # {50, 20, 40, 10, 60, 30}

# dictionary merging --> only 1 way
d1 = {1: "IronMan", 2: "BatMan"}
d2 = {3: "Hulk", 4: "Thor"}
# print(d1 + d2)  # TypeError: unsupported operand type(s) for +: 'dict' and 'dict'
# Note: only keys will be merged
print({*d1, *d2})  # {1, 2, 3, 4}
# Note: keyword args will merge dict key and values
print({**d1, **d2})  # {1: 'IronMan', 2: 'BatMan', 3: 'Hulk', 4: 'Thor'}
