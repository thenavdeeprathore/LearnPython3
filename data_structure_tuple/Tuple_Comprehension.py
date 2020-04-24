"""
Tuple Comprehensions:
-------------------
Tuple Comprehension is not supported by Python.
t = ( x**2 for x in range(1,6))
Here we are not getting tuple object and we are getting generator object
"""

# Tuple Comprehension is not supported by Python
x = (i for i in range(0, 10))
print(x)  # <generator object <genexpr> at 0x00834680>
