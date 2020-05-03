# REVERSE internal content of every second word present in the given string

my_string = "one two three four five six"
print(my_string)  # one two three four five six
my_list = my_string.split()
print(my_list)  # ['one', 'two', 'three', 'four', 'five', 'six']
empty_list = []
i = 0

while i < len(my_list):
    if i % 2 == 0:
        empty_list.append(my_list[i])
    else:
        empty_list.append(my_list[i][::-1])
    i = i + 1
print(empty_list)  # ['one', 'owt', 'three', 'ruof', 'five', 'xis']
output = ' '.join(empty_list)
print(output)  # one owt three ruof five xis
