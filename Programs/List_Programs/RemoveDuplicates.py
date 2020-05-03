my_list = [30, 10, 40, 20, 10, 20, 50, 30]

print("The original list is : ", my_list)

# Method 1 : Naive methods
other_list = []

for x in my_list:
    if x not in other_list:
        other_list.append(x)
print("The list after removing duplicates : ", other_list)

# Method 2 : Using list comprehension
[other_list.append(x) for x in my_list if x not in other_list]
print("The list after removing duplicates : ", other_list)

# Method 3 : Using set()
# Insertion order will not be preserved
other_list = list(set(my_list))
print("The list after removing duplicates : ", other_list)

# Method 4 : Using collections.OrderedDict.fromkeys()
from collections import OrderedDict

# using collections.OrderedDict.fromkeys() to remove duplicated
other_list = list(OrderedDict.fromkeys(my_list))
print("The list after removing duplicates : ", other_list)
