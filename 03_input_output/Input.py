"""
Reading Dynamic Input from the Keyboard:
----------------------------------------
In Python 2 the following 2 functions are available to read dynamic input from the keyboard.
1) raw_input()
2) input()

***Note:
-------
=>  But in Python 3 we have only input() method and raw_input() method is not available.
=>  Python3 input() function behaviour exactly same as raw_input() method of Python2.
    i.e every input value is treated as str type only.
=>  raw_input() function of Python 2 is renamed as input() function in Python 3.

Python3 input():
---------------
=>  This function always reads the data from the keyboard in the form of String Format.
=>  We have to convert that string type to our required type by using the corresponding
    type casting methods.

=>  Eg: x = input("Enter First Number:")
    print(type(x))  It will always print str type only for any input type
"""
# case 1: Write a program to read 2 numbers from the keyboard and print sum
x = input("Enter First Number: ")
y = input("Enter Second Number: ")
i = int(x)
j = int(y)
print("The sum is: ", i + j)

# case 2:
x = int(input("Enter First Number: "))
y = int(input("Enter Second Number: "))
print("The sum is: ", x + y)

# case 3:
print("The sum is: ", int(input("Enter First Number: ")) + int(input("Enter Second Number: ")))

# case 4:
a = input("Enter a string: ")
print(type(a))  # <class 'str'>
b = int(input("Enter a int: "))
c = float(input("Enter a float: "))
d = bool(input("Enter a boolean: "))
print(a)
print(b)
print(c)
print(d)

# cse 5: To convert st to bool type we should use eval() instead of bool()
e = eval(input("Enter a boolean: "))
print(e)

# case 6: How to read multiple values from the keyboard in a single line:
a, b = [int(x) for x in input("Enter 2 numbers :").split()]
print("Product is :", a * b)
# Note: split() function can take space as separator by default but we can pass anything as separator.

# case 7: Write a program to read 3 float numbers from the keyboard with, seperator and print their sum
a, b, c = [float(x) for x in input("Enter 3 float numbers :").split(',')]
print("The Sum is :", a + b + c)
