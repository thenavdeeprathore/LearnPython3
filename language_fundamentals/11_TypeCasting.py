"""
Type Casting:
------------
We can convert one type value to another type. This conversion is called Typecasting or Type coersion.

The following are various inbuilt functions for type casting.
1) int()
2) float()
3) complex()
4) bool()
5) str()
"""

# int()
"""
Note:
1) We can convert from any type to int except complex type.
2) If we want to convert str type to int type, compulsory str should contain only integral
value and should be specified in base-10.
"""
print(int(12.456))  # 12
# print(int(10+20j))  # TypeError: can't convert complex to int
print(int("10") + 10)  # 20
# print(int("hello"))  # ValueError: invalid literal for int() with base 10: 'hello'
# print(int("10.5"))  # ValueError: invalid literal for int() with base 10: '10.5'
print(int(True))  # 1
print(int(False))  # 0


# float()
"""
We can use float() function to convert other type values to float type.

Note:
1) We can convert any type value to float type except complex type.
2) Whenever we are trying to convert str type to float type compulsory str should be
either integral or floating point literal and should be specified only in base-10. 
"""
print(float(10))  # 10.0
print(float(10.5))  # 10.5
# print(float(10+20j))  # TypeError: can't convert complex to float
print(float("10"))  # 10.0
print(float("10.20"))  # 10.2
print(float(True))  # 1.0
print(float(False))  # 0.0


# bool()
"""
We can use this function to convert other type values to bool type.
"""
print(bool(0))  # False
print(bool(1))  # True
print(bool(10))  # True
print(bool(10.5))  # True
print(bool(0.008))  # False
print(bool(0.0))  # False
print(bool(True))  # True
print(bool(False))  # False
print(bool(-0.0123))  # True
print(bool(0+0j))  # False
print(bool(1+0j))  # True
print(bool(""))  # False
print(bool())  # False
print(bool("yes"))  # True
print(bool("no"))  # True
print(bool('True'))  # True
print(bool('False'))  # True





