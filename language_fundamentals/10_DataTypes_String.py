"""
# A string is a sequence of characters. A character is simply a symbol.
# Python does not have a character data type,
a single character is simply a string with a length of 1

A String is a sequence of characters enclosed within single quotes or double quotes or triple quotes.
"""

char_str = 'a'
print(char_str)

str1 = 'single quote'
print(str1)

str2 = "double quote"
print(str2)

str3 = '''
triple single quote
'''
print(str3)

str4 = """
triple double quote
"""
print(str4)

"""
We can also use triple quotes to use single quote or double quote in our String.
=> ''' This is " character'''
    ' This i " Character '
=> We can embed one string in another string
=> '''This "Python class very helpful" for java students'''
=> To define doc string
"""

"""
Slicing of Strings:
-------------------
1) slice means a piece
2) [ ] operator is called slice operator, which can be used to retrieve parts of String.
3) In Python Strings follows zero based index.
4) The index can be either +ve or -ve.
5) +ve index means forward direction from Left to Right
6) -ve index means backward direction from Right to Left
"""

s = "python"
print(s[0])
print(s[-1])
# print(s[100])  # IndexError: string index out of range


# + and * operators for str data types:
print("Hello" + "World")
# print("hello" + 10)  # TypeError: can only concatenate str (not "int") to str
print("Hello" + str(10))  # Hello10

print("Tom"*3)  # TomTomTom
# print("Tom"*"Jerry")  # TypeError: can't multiply sequence by non-int of type 'str'


"""
Note:
1) In Python the following data types are considered as Fundamental Data types
- int
- float
- complex
- bool
- str

2) In Python, we can represent char values also by using str type and explicitly char type
is not available.
>>> c='a'
>>> type(c)
<class 'str'>

3) long Data Type is available in Python2 but not in Python3. In Python3 long values also
we can represent by using int type only.

"""



