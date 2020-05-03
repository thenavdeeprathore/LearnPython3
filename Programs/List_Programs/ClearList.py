# Method 1 : Using clear() method

# Creating list
my_list = [6, 0, 4, 1]
print('my_list before clear: ', my_list)

# Clearing list
my_list.clear()
print('my_list after clear: ', my_list)

# Method 2 : Reinitializing the list
my_list = [6, 0, 4, 1, 5, 8]
print('my_list before reinitialization: ', my_list)

my_list = []
print('my_list after clearing using reinitialization: ', my_list)

# Method 3 : Using “*= 0”
my_list = [6, 0, 4, 1]
print('my_list before clear:', my_list)

# Clearing list
my_list *= 0
print('my_list after clearing using *= 0: ', my_list)

# Method 4 : Using del
# Creating list
my_list = [7, 8, 4, 2]
print('my_list before delete: ', my_list)

# Deleting list
del my_list[:]
print('my_list after delete: ', my_list)
