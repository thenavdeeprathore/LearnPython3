my_list = [30, 10, 40, 20]

# We can sort the list using Python3 in-built function sort() and sorted()

# Sort list - ascending order
my_list.sort()
print("Sorted list ascending: ", my_list)

# Sort list - ascending order
sorted(my_list)
print("Sorted list ascending: ", my_list)

# Sort list - descending order/reversed order
my_list.sort(reverse=True)
print("Sorted list descending: ", my_list)

# Sort list - descending order/reversed order
sorted(my_list, reverse=True)
print("Sorted list descending: ", my_list)
