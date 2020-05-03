# Various ways to find length of the list

# 1
test_list = [1, 4, 5, 7, 8]

# Printing test_list
print("The list is : ", test_list)

counter = 0
for i in test_list:
    # incrementing counter
    counter = counter + 1

# Printing length of list
print("Length of list using naive method is : " + str(counter))

# 2
print("Length of list using len function : ", len(test_list))
