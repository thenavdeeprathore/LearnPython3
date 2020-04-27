"""
Nested Tuples:
-------------
Tuple inside another tuple is called nested tuple

Tuple of Tuples:
-------------
import itertools
tuple(itertools.chain(*tupleName))
"""

n = (10, 20, (30, 40))
print(n)  # (10, 20, (30, 40))
print(n[0])  # 10
print(n[1])  # 20
print(n[2])  # (30, 40)
print(n[2][0])  # 30
print(n[2][1])  # 40

# Nested Tuple as Matrix:
n = ((10, 20, 30), (40, 50, 60), (70, 80, 90))
print(n)  # ((10, 20, 30), (40, 50, 60), (70, 80, 90))
print("Elements by row wise: ")
for row in n:
    print(row)

# Elements by row wise:
# (10, 20, 30)
# (40, 50, 60)
# (70, 80, 90)

print("Elements by Matrix style: ")
for row in n:
    for col in row:
        print(col, end=' ')
    print()

# Elements by Matrix style:
# 10 20 30
# 40 50 60
# 70 80 90

# Convert nested tuples into normal tuple:
import itertools

tuple1 = ((1, 2, 3), (4, 5), (6,), (7, 8, 9), (0,))
print(tuple1)  # ((1, 2, 3), (4, 5), (6,), (7, 8, 9), (0,))

tuple2 = tuple(itertools.chain(*tuple1))
print(tuple2)  # (1, 2, 3, 4, 5, 6, 7, 8, 9, 0)
