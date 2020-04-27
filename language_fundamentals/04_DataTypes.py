"""
- Data Type represents the type of data present inside a variable.
- In Python we are not required to specify the type explicitly. Based on value provided,
the type will be assigned automatically. Hence Python is dynamically Typed Language.
"""
# 14 inbuilt Data Types:
"""
int
float
complex
bool
str
bytes
bytearray
range
list
tuple
set
frozenset
dict
None
"""

# Note: In Python everything is an object

a = 10
print(type(a))  # int
b = 23.45
print(type(b))  # float
c = 'Tom'
print(type(c))  # str
d = "Chris"
print(type(d))  # str
e = """
Hi
Hello
How are you
"""
print(type(e))  # str
f = True
print(type(f))  # bool
g = False
print(type(g))  # bool

x = 100
y = 100
z = 200
print(id(x))
print(id(y))
print(id(z))

