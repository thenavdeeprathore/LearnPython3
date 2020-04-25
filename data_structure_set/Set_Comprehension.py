"""
Set Comprehensions:
-------------------
Set Comprehension is possible
"""

# square
s = {x * x for x in range(1, 6)}
print(s)  # {1, 4, 9, 16, 25}
print(type(s))  # <class 'set'>

# 2 power
s = {2 * x for x in range(1, 6)}
print(s)  # {2, 4, 6, 8, 10}
print(type(s))  # <class 'set'>

# remove duplicates in list
l = [10, 20, 10, 20, 30]
s = set(l)
print(s)  # {10, 20, 30}
l = list(s)
print(l)  # [10, 20, 30]

# Write a Program to Print different Vowels Present in the given Word?
w = input("Enter word to search for vowels: ")
s = set(w)
v = {'a', 'e', 'i', 'o', 'u'}
d = s.intersection(v)
print("The different vowel present in", w, "are", d)
