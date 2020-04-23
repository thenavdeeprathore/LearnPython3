"""
List Comprehensions:
-------------------
It is very easy and compact way of creating list objects from any iterable objects
(Like List, Tuple, Dictionary, Range etc) based on some condition.

Syntax: list = [expression for item in list if condition]
"""

# Way 1:
list_of_numbers = [i for i in range(0, 10)]
print(list_of_numbers)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Way 2: Much easier
list_of_range = list(range(10))
print(list_of_range)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Even numbers less than 10
list_of_even = [i for i in range(0, 10, 2)]
print(list_of_even)  # [0, 2, 4, 6, 8]

list_of_even_range = list(range(0, 10, 2))
print(list_of_even_range)  # [0, 2, 4, 6, 8]

# program 1: square number list
list_square = [x * x for x in range(1, 11)]
print(list_square)  # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# program 2: 2 power list
list_power = [2 ** x for x in range(1, 11)]
print(list_power)  # [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]

# program 3: divisible by ten
list_10_divisible = [x for x in range(1, 101) if x % 10 == 0]
print(list_10_divisible)  # [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# program 4: list1 doesn't contain list2 items
num1 = [10, 20, 30, 40]
num2 = [30, 40, 50, 60]
num3 = [x for x in num1 if x not in num2]
print(num3)  # [10, 20]

# program 5: fetch only first word from each list items
city = ['Mumbai', 'Pune', 'Tokyo', 'London']
first_word = [x[0] for x in city]
print(first_word)  # ['M', 'P', 'T', 'L']

# program 6: split string into list
words = "the quick brown fox jumps over the lazy dog".split()
print(words)  # ['the', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']
list_count = [[x.upper(), len(x)] for x in words]
print(list_count)
# [['THE', 3], ['QUICK', 5], ['BROWN', 5], ['FOX', 3], ['JUMPS', 5], ['OVER', 4], ['THE', 3], ['LAZY', 4], ['DOG', 3]]


# Q) Write a Program to display unique vowels {a, e, i, o, u} present in the given Word?
# without list comprehension
vowels = ['a', 'e', 'i', 'o', 'u']
s = input("Enter a string value: ")
result = []
for letter in s:
    if letter in vowels:
        if letter not in result:
            result.append(letter)

print(result)
print(f"The number of unique vowels present in {s} is {len(result)}")

# with list comprehension
vowels = ['a', 'e', 'i', 'o', 'u']
s = input("Enter a string value: ")
result = [letter for letter in vowels if letter in s]
print(result)
print(f"The number of unique vowels present in {s} is {len(result)}")
