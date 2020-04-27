# How to check a particular File exists OR not?
"""
We can use os library to get information about files in our computer.

os module has path sub module,which contains isFile() function to check whether a
particular file exists or not?
 os.path.isfile(fname)
"""

import os

fname = input("Enter File Name: ")
if os.path.isfile(fname):
    print("File exists: ", fname)
    f = open(fname, "r")
    data = f.read()
    print("The content of the file is: ")
    print("*" * 40)
    print(data)
    print("*" * 40)
else:
    print("File doesn't exist: ", fname)
