"""
tell():
- We can use tell() method to return current position of the cursor(file pointer) from
beginning of the file. [ can you please tell current cursor position]
- The position(index) of first character in files is zero just like string index
"""

f = open("abc.txt", 'r')
print(f.tell())  # 0
print(f.read(2))
print(f.tell())  # 2
print(f.read(3))
print(f.tell())  # 5


"""
seek():

We can use seek() method to move cursor (file pointer) to specified location.
[Can you please seek the cursor to a particular location]

f.seek(offset, fromwhere)  offset represents the number of positions

The allowed Values for 2nd Attribute (from where) are
0  From beginning of File (Default Value)
1  From Current Position
2  From end of the File

Note: Python 2 supports all 3 values but Python 3 supports only 0  From beginning of File (Default Value)
"""
f = open("abc.txt", 'r')
print(f.tell())  # 0
print(f.seek(3))  # 3
print(f.tell())  # 3
print(f.read(2))  # de
print(f.seek(20))  # 20
print(f.read())
print(f.seek(0))
print(f.read())

