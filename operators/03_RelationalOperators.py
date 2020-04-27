"""
2) Relational Operators: >, >=, <, <=
-------------------------------------
We can apply relational operators for int and str types also.

"""

# int
a = 10
b = 20
print("a > b is ", a > b)
print("a >= b is ", a >= b)
print("a < b is ", a < b)
print("a <= b is ", a <= b)

# str
i = 'a'
j = 'b'
print("i > j is ", i > j)
print("i >= j is ", i >= j)
print("i < j is ", i < j)
print("i <= j is ", i <= j)

print(ord('a'))  # 97
print(ord('b'))  # 98

print(ord('A'))  # 65
print(ord('B'))  # 66

print(chr(97))  # a

# case 1:
s1 = "vicky"
s2 = "sunny"
print(s1 > s2)  # True
print(s1 >= s2)  # True
print(s1 < s2)  # False
print(s1 <= s2)  # False

# case 2:
s1 = "sunny"
s2 = "sunny"
print(s1 > s2)  # False
print(s1 >= s2)  # True
print(s1 < s2)  # False
print(s1 <= s2)  # True

# case 3:
s1 = "sunny"
s2 = "Sunny"
print(s1 > s2)  # True
print(s1 >= s2)  # True
print(s1 < s2)  # False
print(s1 <= s2)  # False

# bool
print(True > True)  # False
print(True >= True)  # True
print(10 > True)  # True
print(False > True)  # False

# print(10 > 'sunny')  # TypeError: '>' not supported between instances of 'int' and 'str'


# Note: Chaining of relational operators is possible.
# In the chaining, if all comparisons returns True then only result is True.
# If at-least one comparison returns False then the result is False.
print(10 < 20)  # True
print(10 < 20 < 30)  # True
print(10 < 20 < 30 < 40)  # True
print(10 < 20 < 30 < 40 > 50)  # False
