# Closing a File:
"""
# After completing our operations on the file, it is highly recommended to close the file.
# For this we have to use close() function.
# f.close()

f = open('abc.txt', 'mode')
# perform required write or read operations
f.close()

- Whenever we are closing the file, all system resources which are associated with that file
  will be released
- If we are not closing the file, then there may be performance issues


Various Properties of File Object:
---------------------------------
Once we opened a file and we got file object, we can get various details related to that file
by using the following attributes and methods

f = open('abc.txt', 'w')

- name  Name of the opened file
- mode  Mode in which the file is opened
- closed  Returns boolean value, indicates that whether file is closed or not
- readable() Returns boolean value, indicates that whether file is readable or not
- writable() Returns boolean value, indicates that whether file is writable or not.
"""


# default mode
f = open("abc.txt")
# variables
print("File Name: ", f.name)
print("File Mode: ", f.mode)
print("Is File Closed : ", f.closed)
# methods
print("Is File Readable: ", f.readable())
print("Is File Writable: ", f.writable())
f.close()
print("Is File Closed : ", f.closed)


# read
f = open("abc.txt", 'r')
# variables
print("File Name: ", f.name)
print("File Mode: ", f.mode)
print("Is File Closed : ", f.closed)
# methods
print("Is File Readable: ", f.readable())
print("Is File Writable: ", f.writable())
f.close()
print("Is File Closed : ", f.closed)


# write
f = open("abc.txt", 'w')
# variables
print("File Name: ", f.name)
print("File Mode: ", f.mode)
print("Is File Closed : ", f.closed)
# methods
print("Is File Readable: ", f.readable())
print("Is File Writable: ", f.writable())
f.close()
print("Is File Closed : ", f.closed)


# read and write
f = open("abc.txt", 'r+')
# variables
print("File Name: ", f.name)
print("File Mode: ", f.mode)
print("Is File Closed : ", f.closed)
# methods
print("Is File Readable: ", f.readable())
print("Is File Writable: ", f.writable())
f.close()
print("Is File Closed : ", f.closed)


# write and read
f = open("abc.txt", 'w+')
# variables
print("File Name: ", f.name)
print("File Mode: ", f.mode)
print("Is File Closed : ", f.closed)
# methods
print("Is File Readable: ", f.readable())
print("Is File Writable: ", f.writable())
f.close()
print("Is File Closed : ", f.closed)


# append
f = open("abc.txt", 'a')
# variables
print("File Name: ", f.name)
print("File Mode: ", f.mode)
print("Is File Closed : ", f.closed)
# methods
print("Is File Readable: ", f.readable())
print("Is File Writable: ", f.writable())
f.close()
print("Is File Closed : ", f.closed)


# append and read
f = open("abc.txt", 'a+')
# variables
print("File Name: ", f.name)
print("File Mode: ", f.mode)
print("Is File Closed : ", f.closed)
# methods
print("Is File Readable: ", f.readable())
print("Is File Writable: ", f.writable())
f.close()
print("Is File Closed : ", f.closed)
