from collections import OrderedDict


def remove_duplicates_without_order(str):
    return "".join(set(str))


def remove_duplicates_with_order(str):
    return "".join(OrderedDict.fromkeys(str))


my_string = "hello pp python"
my_char = "hellopptpfptpspttp"
my_number = 1234567895555425
print(my_string)
print(my_char)
print(my_number)

print(remove_duplicates_without_order(my_string))

print(remove_duplicates_with_order(my_string))
print(remove_duplicates_with_order(my_char))
print(remove_duplicates_with_order(str(my_number)))
