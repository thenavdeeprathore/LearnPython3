# from import
"""
We can import particular members of module by using from ... import .
The main advantage of this is we can access members directly without using module name.
"""

from mymath import x, add

print(x)  # 100
add(10, 20)  # The Sum: 30
# product(10, 20)  # NameError: name 'product' is not defined


# Note:
# We can import all members of a module by using --> from mymath import *


from mymath import *

print(x)  # 100
add(10, 20)  # The Sum: 30
product(10, 20)  # The Product: 200
