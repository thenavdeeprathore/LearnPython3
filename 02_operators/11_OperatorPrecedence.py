"""
Operator Precedence:
--------------------
If multiple operators present then which operator will be evaluated first is decided by
operator precedence.

Eg:
print(3+10*2)  23
print((3+10)*2)  26

The following list describes operator precedence in Python
----------------------------------------------------------
1) ()  Parenthesis
2) **  Exponential Operator
3) ~, -  Bitwise Complement Operator, Unary Minus Operator
4) *, /, %, //  Multiplication, Division, Modulo, Floor Division
5) +, -  Addition, Subtraction
6) <<, >>  Left and Right Shift
7) &  Bitwise And
8) ^  Bitwise X-OR
9) |  Bitwise OR
10) >, >=, <, <=, ==, !=  Relational OR Comparison Operators
11) =, +=, -=, *=...  Assignment Operators
12) is , is not  Identity Operators
13) in , not in  Membership operators
14) not  Logical not
15) and  Logical and
16) or  Logical or
"""
# case 1:
a = 30
b = 20
c = 10
d = 5
print((a + b) * c / d)  # 100.0
print((a + b) * (c / d))  # 100.0
print(a + (b * c) / d)  # 70.0

# case 2:
print(3 / 2 * 4 + 3 + (10 / 5) ** 3 - 2)
# 3 / 2 * 4 + 3 + 8.0 - 2
# 15.0
