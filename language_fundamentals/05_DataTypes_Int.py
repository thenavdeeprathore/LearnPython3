# int:
"""
int Data Type:
We can use int data type to represent whole numbers (integral values)
Eg: a = 10
 type(a) #int
Note:
- In Python2 we have long data type to represent very large integral values.
- But in Python3 there is no long type explicitly and we can represent long values also by
using int type only.

We can represent int values in the following ways:
1) Decimal form
2) Binary form
3) Octal form
4) Hexa decimal form
"""

a = 10  # decimal
b = 0b10  # binary
c = 0o10  # octal
d = 0X10  # hexadecimal
print(a)
print(b)
print(c)
print(d)

"""
I) Decimal Form (Base-10):
- It is the default number system in Python
- The allowed digits are: 0 to 9
- Eg: a =10
"""
d = 10
print("Decimal: ", d)

"""
II) Binary Form (Base-2):
- The allowed digits are : 0 & 1
- Literal value should be prefixed with 0b or 0B
- Eg: a = 0B1111
 a = 0B111
 a = 0b111
"""
b = 0B1111
print("Binary: ", b)
b = 0b111
print("Binary: ", b)

"""
III) Octal Form (Base-8):
- The allowed digits are : 0 to 7
- Literal value should be prefixed with 0o or 0O.
- Eg: a = 0o123
 a = 0o786
"""
o = 0o123
print("Octal: ", o)
o = 0O111
print("Octal: ", o)

"""
IV) Hexa Decimal Form (Base-16):
- The allowed digits are: 0 to 9, a-f (both lower and upper cases are allowed)
- Literal value should be prefixed with 0x or 0X
- Eg: a = 0XFACE
 a = 0XBeef
 a = 0XBeer
"""
h = 0xBeef
print("Hexadecimal: ", h)
h = 0X10
print("Hexadecimal: ", h)

# Note: Being a programmer we can specify literal values in decimal, binary, octal and hexa
# decimal forms. But PVM will always provide values only in decimal form.
a = 10
b = 0o10
c = 0X10
d = 0B10
print(a)  # 10
print(b)  # 8
print(c)  # 16
print(d)  # 2
