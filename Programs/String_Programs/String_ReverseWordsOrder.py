# REVERSE order of words present in the given string

my_string = "Learning Python Is Very Easy"
print(my_string)
my_list = my_string.split()
print(my_list)
reverse_list = my_list[::-1]
print(reverse_list)
output = ' '.join(reverse_list)
print(output)


