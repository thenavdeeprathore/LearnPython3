"""
Reading Character Data from Text Files:
We can read character data from text file by using the following read methods.

read() To read total data from the file
read(n)  To read 'n' characters from the file
readline() To read only one line
readlines() To read all lines into a list
"""

# read()
f = open("../Python_FileHandling/abcd.txt", "r")
data = f.read()
print(data)
f.close()
print("***** read operations are completed *****")
# sunny
# katrina
# kiara
# deepika


# read() -- default mode "r"
f = open("../Python_FileHandling/abcd.txt")
data = f.read()
print(data)
f.close()
print("***** read operations are completed *****")
# sunny
# katrina
# kiara
# deepika


# read(n) -- \n will also be calculated as char
f = open("../Python_FileHandling/abcd.txt")
data = f.read(10)
print(data)
f.close()
print("***** read(n) operations are completed *****")
# sunny
# katr


# read(n) -- with negative value -- we will get total file content
f = open("../Python_FileHandling/abcd.txt")
data = f.read(-1)
print(data)
f.close()
print("***** read(-n) operations are completed *****")
# sunny
# katrina
# kiara
# deepika


# read(n) -- with larger count like 100000000 -- only available characters we will get
f = open("../Python_FileHandling/abcd.txt")
data = f.read(100000000)
print(data)
f.close()
print("***** read(nnnnnnnnn) operations are completed *****")
# sunny
# katrina
# kiara
# deepika
# f.read(100000000)  # It will ignore unnecessary count if there is no data present


# readline()
f = open("../Python_FileHandling/abcd.txt", "r")
row1 = f.readline()
print("Firs row: ", row1, end="")
row2 = f.readline()
print("Second row: ", row2, end="")
f.close()
print("***** readline() operations are completed *****")
# Firs row:  sunny
# Second row:  katrina


# readline() using loop
f = open("../Python_FileHandling/abcd.txt", "r")
row = f.readline()
while row != '':
    print(row, end='')
    row = f.readline()

f.close()
print("\n***** readline() wil loop operations are completed *****")
# sunny
# katrina
# kiara
# deepika


# readlines() -- To read all lines into a list
f = open("../Python_FileHandling/abcd.txt", "r")
list = f.readlines()
print(list)
f.close()
print("***** readlines() operations are completed *****")
# ['sunny\n', 'katrina\n', 'kiara\n', 'deepika']


# readlines() -- To read all lines into a list items
f = open("../Python_FileHandling/abcd.txt", "r")
list = f.readlines()
for item in list:
    print(item, end='')

f.close()
print("\n***** readlines() with loop operations are completed *****")


# case 1: Not a good programming practise
f = open("../Python_FileHandling/abcd.txt", "r")
print(f.read(3))
print(f.readline())
print(f.readline())
print(f.read())
f.close()


