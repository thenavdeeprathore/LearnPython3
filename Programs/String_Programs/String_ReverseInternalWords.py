# REVERSE internal content of each word

my_string = "Learning Python Is Very Easy"
print(my_string)  # Learning Python Is Very Easy
my_list = my_string.split()
print(my_list)  # ['Learning', 'Python', 'Is', 'Very', 'Easy']
empty_list = []

for word in my_list:
    empty_list.append(word[::-1])
print(empty_list)  # ['gninraeL', 'nohtyP', 'sI', 'yreV', 'ysaE']
output = ' '.join(empty_list)
print(output)  # gninraeL nohtyP sI yreV ysaE

