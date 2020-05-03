my_list = [30, 10, 40, 20]

# Max
print("Max: ", max(my_list))
my_list.sort(reverse=True)
print("Max: ", my_list[:1])

# Min
print("Min: ", min(my_list))
my_list.sort()
print("Min: ", my_list[:1])
