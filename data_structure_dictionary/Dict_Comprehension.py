"""
Dictionary Comprehension:
------------------------
Comprehension concept is applicable for dictionaries.
"""

squares = {x: x * x for x in range(1, 6)}
print(squares)  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

doubles = {x: 2 * x for x in range(1, 6)}
print(doubles)  # {1: 2, 2: 4, 3: 6, 4: 8, 5: 10}
