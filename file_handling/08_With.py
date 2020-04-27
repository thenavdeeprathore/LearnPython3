# The with statement:
"""
- The with statement can be used while opening a file. We can use this to group file
operation statements within a block.

- The advantage of with statement is it will take care closing of file, after completing all
operations automatically
- Even in the case of exceptions also we are not required to close explicitly.
"""

# In this case file will be close automatically
with open("abc.txt", "w") as f:
    f.write("Navdeep\n")
    f.write("Singh\n")
    f.write("Rathore\n")
    print("Is File Closed: ", f.closed)
print("Is File Closed: ", f.closed)


# f = open("abc.txt", "w")
# In this case we have to close the file explicitly
