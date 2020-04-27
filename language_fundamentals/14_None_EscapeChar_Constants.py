"""
None Data Type:

=> None means nothing or No value associated.
=> If the value is not available, then to handle such type of cases None introduced.
=> It is something like null value in Java.

=> Only one object got created by PVM which is None
"""


def m1():
    a = 10


print(m1())  # None

x = None
print(id(x))


# Escape characters:
"""
The following are various important escape characters in Python
1) \n  New Line
2) \t  Horizontal Tab
3) \r  Carriage Return
4) \b  Back Space
5) \f  Form Feed
6) \v  Vertical Tab
7) \'  Single Quote
8) \"  Double Quote
9) \\  Back Slash Symbol

"""

# Constants
"""
Constants:
- Constants concept is not applicable in Python.
- But it is convention to use only uppercase characters if we don’t want to change value.
- MAX_VALUE = 10
- It is just convention but we can change the value.
"""
print("hello\nworld")
print("hello\tworld")
print('hello\'world')
print("hello\"world")
print("""hello"world""")
print('''hello'world''')
