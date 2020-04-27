"""
string      --> list conversion
numbers     --> list conversion
tuple       --> list conversion
set         --> list conversion
dictionary  --> list conversion
"""
# Convert String --> List
one_word_string = "Hello"
one_word_string_into_list = list(one_word_string)
print(one_word_string_into_list)  # ['H', 'e', 'l', 'l', 'o']

two_word_string = "Hello World"
two_word_string_into_list = list(two_word_string)
print(two_word_string_into_list)  # ['H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd']

# Convert Numbers --> List
numbers = 12345
# numbers_into_list = list(numbers)  # TypeError: 'int' object is not iterable
numbers_into_list = list(str(numbers))
print(numbers_into_list)  # ['1', '2', '3', '4', '5']

# Convert Tuple --> List
number_tuple = (1, 2, 3, 4)
number_tuple_into_list = list(number_tuple)
print(number_tuple_into_list)  # [1, 2, 3, 4]

# Convert Set --> List
number_set = {10, 20, 30, 40}
number_set_into_list = list(number_set)
print(number_set_into_list)  # [40, 10, 20, 30]

# Convert Dictionary --> List
my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
key_list = list(my_dict.keys())
print(key_list)  # ['a', 'b', 'c', 'd']
values_list = list(my_dict.values())
print(values_list)  # [1, 2, 3, 4]
