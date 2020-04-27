"""
string      --> set conversion
numbers     --> set conversion
list        --> set conversion
tuple       --> set conversion
dictionary  --> set conversion
"""
# Convert String --> set
s = "Hello"
set_s = set(s)
print(set_s)  # {'o', 'l', 'H', 'e'}

ss = "Hello World"
set_ss = set(ss)
print(set_ss)  # {'H', 'r', 'e', ' ', 'l', 'W', 'o', 'd'}

# Convert Numbers --> set
n = 12345
# set_n = set(n)  # TypeError: 'int' object is not iterable
set_n = set(str(n))
print(set_n)  # {'2', '4', '1', '3', '5'}

# Convert List --> set
l = [1, 2, 3, 4]
set_l = set(l)
print(set_l)  # {1, 2, 3, 4}

# Convert Tuple --> set
t = {10, 20, 30, 40}
set_t = set(t)
print(set_t)  # {40, 10, 20, 30}

# Convert Dictionary --> set
my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
key_tuple = set(my_dict.keys())
print(key_tuple)  # {'c', 'a', 'd', 'b'}
values_tuple = set(my_dict.values())
print(values_tuple)  # {1, 2, 3, 4}
