"""
Nested Lists:
-------------
List inside another list is called nested list

List of Lists:
-------------
import itertools
list(itertools.chain(*listName))
"""

n = [10, 20, [30, 40]]
print(n)  # [10, 20, [30, 40]]
print(n[0])  # 10
print(n[1])  # 20
print(n[2])  # [30, 40]
print(n[2][0])  # 30
print(n[2][1])  # 40

# Nested List as Matrix:
n = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]
print(n)
print("Elements by row wise: ")
for row in n:
    print(row)

print("Elements by Matrix style: ")
for row in n:
    for col in row:
        print(col, end=' ')
    print()


# Convert nested Lists into normal list:
import itertools

list1 = [[1, 2, 3], [4, 5], [6], [7, 8, 9], [0]]
print(list1)

list2 = list(itertools.chain(*list1))
print(list2)
