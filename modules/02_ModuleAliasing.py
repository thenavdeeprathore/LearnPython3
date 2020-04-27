# Module Aliasing
"""
Renaming a Module at the time of import

Eg: import mymath as m
- Here mymath is original module name and m is alias name.
- We can access members by using alias name m
"""

# Imagine this is a test file named as -- test.py
import mymath as m

print(m.x)  # 100
m.add(10, 20)  # The Sum: 30
m.product(10, 20)  # The Product: 200

# print(mymath.x)  # NameError: name 'mymath' is not defined


# Note 1:
# Once you defined alias name you can't use original module name
