# Swap first and last element


def swap_list(newList):
    newList[0], newList[-1] = newList[-1], newList[0]
    return newList


my_list = [12, 35, 9, 56, 24]
print(my_list)
print(swap_list(my_list))


# Swap any two element


def swap_positions(list, pos1, pos2):
    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list


my_list = [23, 65, 19, 90]
pos1, pos2 = 1, 3

print(my_list)
print(swap_positions(my_list, pos1 - 1, pos2 - 1))
