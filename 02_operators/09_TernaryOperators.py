"""
8) Ternary Operator OR Conditional Operator
-------------------------------------------
Syntax: x = firstValue if condition else secondValue
If condition is True then firstValue will be considered else secondValue will be considered.

Note: Nesting of Ternary Operator is Possible.
"""
# case 1:
a, b = 10, 20
x = 30 if a < b else 40
print(x)  # 30

# case 2: Read two numbers from the keyboard and print minimum value
a, b = 10, 20
min = a if a < b else b
print("Min value: ", min)  # Min value:  10

# case 3: Write Program for Minimum of 3 Numbers
a, b, c = 10, 7, 5
min = a if a < b and a < c else b if b < c else c
print("Min value: ", min)  # Min value:  5

# case 4: Read two numbers from the keyboard and print minimum value
a, b = 10, 20
min = a if a < b else b
print("Min value: ", min)  # Min value:  10

# case 5: Write Program for Maximum of 3 Numbers
a, b, c = 10, 7, 5
max = a if a > b and a > c else b if b > c else c
print("max value: ", max)  # max value:  10

# case 6:
a, b = 10, 20
result = "both numbers are equal" if a == b else "first number is less than second number" \
    if a < c else "second number is bigger than first number"
print(result)  # second number is bigger than first number
