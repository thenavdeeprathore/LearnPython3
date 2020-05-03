my_list = [30, 10, 40, 20]

# 1: Print List with reversed Insertion order
print(list(reversed(my_list)))

# 2: Another way to print List with reversed Insertion order
my_list.reverse()
print(my_list)


# 3: Reversing a list using slicing technique
def Reverse(lst):
    new_lst = lst[::-1]
    return new_lst


lst = [10, 11, 12, 13, 14, 15]
print(Reverse(lst))

# Print List Items with reversed Insertion order
for x in reversed(my_list):
    print(x)
