# Working with random Module:
"""
This module defines several functions to generate random numbers.

We can use these functions while developing games, in cryptography and to generate
random numbers for authentication {passwords}, for OTP

functions:
----------
random()
uniform()
randint()
randrange()
choice()
"""


# random()
"""
This function always generate some random float value between 0 and 1 ( not inclusive)
- never going to generate 0
- never going to generate 1
0<x<1

random() function won't take any argument
"""

from random import *

print(random())  # 0.6543690379396034

for i in range(5):
    print(random())


# uniform()
"""
It returns random float values between 2 given numbers (not inclusive)
- never going to generate 0
- never going to generate 1

random()  in between 0 and 1 (not inclusive)
uniform(x,y)  in between x and y ( not inclusive)
"""

from random import *

print(uniform(5, 10))
