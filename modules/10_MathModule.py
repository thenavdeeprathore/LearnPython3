# Python provides inbuilt module math.
# This module defines several functions which can be used for mathematical operations.
"""
The main important functions are
1) sqrt(x)
2) ceil(x)
3) floor(x)
4) fabs(x)
5) log(x)
6) sin(x)
7) tan(x)
8) factorial(x)
etc..
"""

# import math
#
# print(dir(math))
# print(help(math))
"""
List of Functions and Constants in Python Math Module:
-------------------------------------------------------
ceil(x)	        Returns the smallest integer greater than or equal to x.
copysign(x, y)	Returns x with the sign of y
fabs(x)	        Returns the absolute value of x
factorial(x)	Returns the factorial of x
floor(x)	    Returns the largest integer less than or equal to x
fmod(x, y)	    Returns the remainder when x is divided by y
frexp(x)	    Returns the mantissa and exponent of x as the pair (m, e)
fsum(iterable)	Returns an accurate floating point sum of values in the iterable
isfinite(x)	    Returns True if x is neither an infinity nor a NaN (Not a Number)
isinf(x)	    Returns True if x is a positive or negative infinity
isnan(x)	    Returns True if x is a NaN
ldexp(x, i)	    Returns x * (2**i)
modf(x)	        Returns the fractional and integer parts of x
trunc(x)	    Returns the truncated integer value of x
exp(x)	        Returns e**x
expm1(x)	    Returns e**x - 1
log(x[, base])	Returns the logarithm of x to the base (defaults to e)
log1p(x)	    Returns the natural logarithm of 1+x
log2(x)	        Returns the base-2 logarithm of x
log10(x)	    Returns the base-10 logarithm of x
pow(x, y)	    Returns x raised to the power y
sqrt(x)	        Returns the square root of x
acos(x)		    Returns the arc cosine of x
asin(x)		    Returns the arc sine of x
atan(x)		    Returns the arc tangent of x
atan2(y, x)	    Returns atan(y / x)
cos(x)		    Returns the cosine of x
hypot(x, y)	    Returns the Euclidean norm, sqrt(x*x + y*y)
sin(x)		    Returns the sine of x
tan(x)		    Returns the tangent of x
degrees(x)	    Converts angle x from radians to degrees
radians(x)	    Converts angle x from degrees to radians
acosh(x)	    Returns the inverse hyperbolic cosine of x
asinh(x)	    Returns the inverse hyperbolic sine of x
atanh(x)	    Returns the inverse hyperbolic tangent of x
cosh(x)		    Returns the hyperbolic cosine of x
sinh(x)		    Returns the hyperbolic cosine of x
tanh(x)		    Returns the hyperbolic tangent of x
erf(x)		    Returns the error function at x
erfc(x)		    Returns the complementary error function at x
gamma(x)	    Returns the Gamma function at x
lgamma(x)	    Returns the natural logarithm of the absolute value of the Gamma function at x
pi		        Mathematical constant, the ratio of circumference of a circle to it's diameter (3.14159...)
e		        mathematical constant e (2.71828...)
"""

from math import *

print(factorial(4))  # 24
print(sqrt(4))  # 2.0
print(fabs(-10.5))  # 10.5
print(fabs(10.7))  # 10.7
print(ceil(10.5))  # 11
print(floor(10.5))  # 10

# find area of the circle
r = int(input("Enter radius: "))  # 10
# area = pi * r ** 2
area = pi * pow(r, 2)
print("Area of circle: ", area)  # Area of circle:  314.1592653589793

# Certification questions:
"""
Question:
A float value passed to the function
The function must take absolute value of the float
Any decimal points after the integer must be removed

Which two math functions should be used?

1) math.frexp(x)
2) math.floor(x)
3) math.fabs(x)
4) math.fmod(x)
5) math.ceil(x)
"""

# Answer:
# math.fabs(x)
# math.floor(x)

f = -25.678
a = fabs(f)
d = floor(a)
print(d)  # 25


"""
Question:
Import statements:

1) import math.sqrt as sq
2) import sqrt from math as sq
3) from math import sqrt as sq
4) from math.sqrt as sq
"""

# Answer:
# 3) from math import sqrt as sq


"""
Question:
Consider the code

import math
l = [str(round(math.pi)) for i in range(1, 6)]
print(l)

A) ['3', '3', '3', '3', '3']
B) ['3', '3', '3', '3', '3', '3']
C) ['1', '2', '3', '4', '5']
D) ['1', '2', '3', '4', '5', '6']
"""

# Answer:
# range(1, 6) means 1 to 5 -- 5 times
# round(3.1415) -- 3
# str(3) -- 5 times
# A) ['3', '3', '3', '3', '3']
