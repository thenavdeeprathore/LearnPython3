"""
1) Arithmetic Operators:
------------------------
Total there are 7 operators

These 5 operators are provided in every programming language
+  Addition
–  Subtraction
*  Multiplication
/  Division Operator
%  Modulo Operator

These 2 operators are only provided in python
//  Floor Division Operator
**  Exponent Operator OR Power Operator

Note 1:
------
- / operator always performs floating point arithmetic. Hence it will always returns float value.
- But Floor division (//) can perform both floating point and integral arithmetic. If
arguments are int type then result is int type. If at least one argument is float type then
result is float type.

Note 2:
-------
- We can use +,* operators for str type also.
- If we want to use + operator for str type then compulsory both arguments should be
str type only otherwise we will get error.
-If we use * operator for str type then compulsory one argument should be int and
other argument should be str type.
    2*"vicky"
    "vicky"*2
    2.5*"vicky"  TypeError: can't multiply sequence by non-int of type 'float'
    "vicky"*"vicky"  TypeError: can't multiply sequence by non-int of type 'str'
֍ +  String Concatenation Operator
֍ *  String Multiplication Operator

Note 3:
------
For any number x,
x/0 and x%0 always raises "ZeroDivisionError"
10/0
10.0/0
"""

a = 10
b = 2
print('a+b=', a + b)  # 12
print('a-b=', a - b)  # 10
print('a*b=', a * b)  # 20
print('a/b=', a / b)  # 5.0
print('a//b=', a // b)  # 5
print('a%b=', a % b)  # 0
print('a**b=', a ** b)  # 100

# difference between division / and floor division // operators
print(10 / 3)  # 3.3333333333333335
print(10.0 / 3)  # 3.3333333333333335
print(10 // 3)  # 3
print(10.0 // 3)  # 3.0

# If arguments are int type then result is int type
print(11 // 2)  # 5
# If at least one argument is float type then result is float type.
print(11.9 // 2)  # 5.0

# exercise:
print(20 / 2)  # 10.0
print(20.5 / 2)  # 10.25
print(20 // 2)  # 10
print(20.5 // 2)  # 10.0


# + operator
print("vicky" + "sunny")  # vickysunny
print(10 + 20)  # 30
# print("vicky" + 10)  # TypeError: can only concatenate str (not "int") to str
print("vicky" + "10")  # vicky10
# print("vicky" + int("10"))  # TypeError: can only concatenate str (not "int") to str


# * operator
print("vicky"*3)  # vickyvickyvicky
print(3*"vicky")  # vickyvickyvicky
print("vicky"*int("3"))  # vickyvickyvicky
# print("vicky"*"sunny")  # TypeError: can't multiply sequence by non-int of type 'str'
print("vicky"*True)  # vicky
print("Vicky"*False)  #
