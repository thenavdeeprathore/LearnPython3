"""
Base Conversions:

Python provide the following in-built functions for base conversions
bin()
oct()
hex()

1) bin():
---------
We can use bin() to convert from any base to binary

2) oct():
---------
We can use oct() to convert from any base to octal

3) hex():
---------
We can use hex() to convert from any base to hexa decimal
"""
# Decimal to Binary
print(bin(15))  # 0b1111

# Octal to Binary
print(bin(0o11))  # 0b1001

# Hexadecimal to Binary
print(bin(0x10))  # 0b10000


# Decimal to Octal
print(oct(10))  # 0o12

# Binary to Octal
print(oct(0B1111))  # 0o17

# Hexadecimal to Octal
print(oct(0X123))  # 0o443
