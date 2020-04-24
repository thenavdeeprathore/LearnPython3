"""
string      --> tuple conversion
numbers     --> tuple conversion
list        --> tuple conversion
set         --> tuple conversion
dictionary  --> tuple conversion
"""
# Convert String --> Tuple
one_word_string = "Hello"
one_word_string_into_tuple = tuple(one_word_string)
print(one_word_string_into_tuple)  # ('H', 'e', 'l', 'l', 'o')

two_word_string = "Hello World"
two_word_string_into_tuple = tuple(two_word_string)
print(two_word_string_into_tuple)  # ('H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd')

# Convert Numbers --> Tuple
numbers = 12345
# numbers_into_tuple = tuple(numbers)  # TypeError: 'int' object is not iterable
numbers_into_tuple = tuple(str(numbers))
print(numbers_into_tuple)  # ('1', '2', '3', '4', '5')

# Convert List --> Tuple
number_list = [1, 2, 3, 4]
number_tuple_into_tuple = tuple(number_list)
print(number_tuple_into_tuple)  # (1, 2, 3, 4)

# Convert Set --> Tuple
number_set = {10, 20, 30, 40}
number_set_into_tuple = tuple(number_set)
print(number_set_into_tuple)  # (40, 10, 20, 30)

# Convert Dictionary --> Tuple
my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
key_tuple = tuple(my_dict.keys())
print(key_tuple)  # ('a', 'b', 'c', 'd')
values_tuple = tuple(my_dict.values())
print(values_tuple)  # (1, 2, 3, 4)
