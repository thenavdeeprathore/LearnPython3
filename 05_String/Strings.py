"""
# A string is a sequence of characters. A character is simply a symbol.
# String is Immutable - modifications are not allowed
# Supports both +ve and -ve indexing
# Python does not have a character data type, a single character is simply a string with a length of 1
"""

# ------------------- Creating a String -------------------
"""
Strings in Python can be created using single quotes or double quotes or even triple quotes.
"""

# all of the following are equivalent
my_string = 'Hello'
print(my_string)
print(type(my_string))  # <class 'str'>

my_string = "Hello"
print(my_string)
print(type(my_string))  # <class 'str'>

# triple quotes string can extend multiple lines
my_string = """Hello, welcome to
           the world of Python"""
print(my_string)
print(type(my_string))  # <class 'str'>

my_string = '''Hello, welcome to
           the world of Python'''
print(my_string)
print(type(my_string))  # <class 'str'>

# ------------------- Accessing characters in String -------------------

# -6 -5 -4 -3 -2 -1
my_string = "Sweden"
# 0 1 2 3 4 5

# Initial String
print("Initial String: ", my_string)
# Printing First character
print("First character of String is: ", my_string[0])
# Printing Last character
print("Last character of String is: ", my_string[-1])

# ------------------- String Slicing -------------------

# str[begin:end]
# str[begin:end:step]
# str[1:10] --> 1 to 9

# begin must be lower
# end must be higher

# slicing 2nd to 5th character
print('str[1:5] = ', my_string[1:5])  # wede

# slicing 6th to 2nd last character
print('str[5:-2] = ', my_string[2:-2])  # ed

print(my_string[1:4:2])  # wd
print(my_string[2:])  # eden
print(my_string[:])  # Sweden
# print(my_string[9])  # IndexError: string index out of range
print(my_string[-2])  # e
print(my_string[-5:-1])  # wede

# No IndexError: string index out of range for string slicing
print(my_string[1:100])

# ------------------- String Functions -------------------
"""
1. len()
2. strip()
3. lstrip()
4. rstrip()
5. count()
6. concat
7. replication
8. split()
9. enumerate
10. endswith()
11. startswith()
12. find()
13. swapcase()
14. index()
15. isalnum()
16. isalpha()
17. isdigit()
18. isupper()
19. islower()
20. isspace()
21. capitalize()
22. replace()
"""

my_string = "    Vicky    "

# len() - length of the string
print(len(my_string))  # 13

# strip() - remove front and end whitespaces
print(len(my_string.strip()))  # 5

my_string = "@@@hello###"

# lstrip() - remove left items
print(my_string.lstrip("@"))

# rstrip() - remove right items
print(my_string.rstrip("#"))

print(my_string.lstrip("@").rstrip("#"))

# id() - check memory address
# is, is not - memory comparison
# ==, != - data comparison
# in, not in - check data is available or not

a = "John"
b = "Tom"
c = "John"
print(id(a))
print(id(b))
print(id(c))
# only in string id with the same value has same id
print(a is b)
print(b is c)
print(a is c)
print(a is not b)
print(a == b)
print(a == c)
print(a != b)
print("oh" in a)
print("ta" in b)
print("ta" not in b)

# formate data - %s
eid, ename, esal = 111, "Jerry", 1332423

print("EmpID=%d EmpName=%s EmpSal=%g" % (eid, ename, esal))
print("Emp id={} Emp name={} Emp sal={}".format(eid, ename, esal))
print("Emp id={0} Emp name={1} Emp sal={2}".format(eid, ename, esal))

# concat
i = "Johnny"
j = "Tom"
k = i + j
print(k)

# replication
ss = i * 3 + j * 2
print(ss)

kk = "sgss"
jj = 324234
# print(kk + jj)  # TypeError: must be str, not int

# relation
print("John" > "Mike")  # False
print("Tom" > "Jerry")  # True
print("Joy" == "Joy")  # True
print("ABC" <= "CDE")  # True
print("Nav" != "nav")  # True

text = "hi my name is navdeep"
print("upper => ", text.upper())
print("lower => ", text.lower())
print("capitalize => ", text.capitalize())
print("join => ", "+".join(text.split()))
print("replace => ", text.replace("navdeep", "vicky"))

text1 = "hi st.hr thank you"
print(text1.split())  # default splitting character is space
print(text1.split("."))

text2 = "pyhton"
print(list(enumerate(text2)))  # [(0, 'p'), (1, 'y'), (2, 'h'), (3, 't'), (4, 'o'), (5, 'n')]
print(tuple(enumerate(text2)))  # ((0, 'p'), (1, 'y'), (2, 'h'), (3, 't'), (4, 'o'), (5, 'n'))

text3 = "pythonpython"
print(text3.count('p'))
print(text3.count("python"))
print(text3.count('p', 2))
print(text3.count('p', 2, 7))

ps = "welcome to python"
print(ps.endswith('python'))
print(ps.endswith('pyt'))
print(ps.endswith('to', 2, 16))
print(ps.startswith("welcome"))
print(ps.find("to"))
print(ps.find("tom"))  # -1
print(ps.index("to"))
# print(ps.index("tom"))  # ValueError: substring not found

ps1 = "Welcome To my World"
print(ps1.swapcase())  # wELCOME tO MY wORLD

ps2 = "welcome user"
print(ps2.isalnum())  # False

ps2 = "dafdsh324"
print(ps2.isalnum())  # True
print(ps2.isalpha())  # False
print(ps2.isdigit())  # False

ps2 = "2524524"
print(ps2.isdigit())  # True

a1 = "Python"
print(a1.isupper())
print(a1.islower())

a2 = "PYTHON"
print(a2.isupper())

a3 = "python"
print(a3.islower())

a4 = "wwrew jl jk"
print(a4.isspace())

a5 = " "
print(a5.isspace())

b1 = "pythonpython"
print(b1.count("p"))
count = 0
for x in b1:
    if x == 'p':
        count = count + 1

print(count)

b2 = "hi my hi nam is hi"
print(b2.count('hi'))

words = b2.split()
count = 0
for x in words:
    if x == 'hi':
        count = count + 1

print(count)


# 4 types of error in string
# NameError : str.substring()
# TypeError : "tom"+10
# IndexError : str = "hi" print(str[10])
# ValueError : str.index("jerry")
