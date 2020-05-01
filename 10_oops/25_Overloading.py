# Polymorphism

"""
Overloading
    - Operator overloading {supports by Python}
    - Methods overloading  {Doesn't support by Python}
    - Constructors overloading {Doesn't support by Python}
Overriding
    - Methods overriding  {supports by Python}
    - Constructors overriding  {supports by Python}
"""

# One name but multiple form is known as polymorphism

# 1) Operator overloading
# In java we don't have operator overloading but in python it is present
# we can use any operator
# same operator but performing different behaviors

print(10 + 20)
print("Hello" + "World")

print(10 * 3)
print("Hello" * 3)


class Book:

    def __init__(self, pages):
        self.pages = pages

    def __add__(self, other):
        return self.pages + other.pages

    def __sub__(self, other):
        return self.pages - other.pages

    def __mul__(self, other):
        return self.pages * other.pages


b1 = Book(300)
b2 = Book(200)
# Without magic methods these operations below will throw an error
print(b1 + b2)  # 500
print(b1 - b2)  # 100
print(b1 * b2)  # 60000

# magic methods for operator overloading which are python predefined words
"""
+ ==> __add__()
- ==> __sub__()
* ==> __mul__()
/ ==> __div__()
% ==> __mod__()
// ==> __floordiv__()
** ==> __pow__()

+= ==> __iadd__()
-= ==> __isub__()
*= ==> __imul__()
/= ==> __idiv__()
%= ==> __imod__()
//= ==> __ifloordiv__()
**= ==> __ipow__()

> : __gt__()
>= : __ge__()
< : __lt__()
<= : __le__()
== : __eq__()
!= : __ne__()
"""


# Overloading > and <= Operators for Student Class Objects:
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    #  greater than
    def __gt__(self, other):
        return self.marks > other.marks

    #  less than and equal to
    def __le__(self, other):
        return self.marks <= other.marks


print("10>20 =", 10 > 20)  # 10>20 = False
s1 = Student("tom", 100)
s2 = Student("jerry", 200)
print("s1>s2=", s1 > s2)  # s1>s2= False
print("s1<s2=", s1 < s2)  # s1<s2= True
print("s1<=s2=", s1 <= s2)  # s1<=s2= True
print("s1>=s2=", s1 >= s2)  # s1>=s2= False


# importance of __str__() method
# Whenever we are trying to print any object reference, internally __str__() method will be called
class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    # override
    def __str__(self):
        # return self.name
        return f'Name is: {self.name} Roll No is: {self.roll_no} Marks is: {self.marks}'


s1 = Student("tom", 1, 95)
s2 = Student("jerry", 2, 99)
print(s1)  # tom Roll No is: 1 Marks is: 95
print(s2)  # jerry Roll No is: 2 Marks is: 99


# Method overloading -- doesn't support by python
class Test:

    def m1(self):
        print("no arg method")

    def m1(self, x):
        print("one arg method")

    def m1(self, x, y):
        print("two arg method")


t = Test()
# t.m1()  # TypeError: m1() missing 2 required positional arguments: 'x' and 'y'
# t.m1(10)  # TypeError: m1() missing 1 required positional argument: 'y'
t.m1(10, 20)  # two arg method


# Constructor overloading -- doesn't support by python
class Test:

    def __init__(self):
        print("no arg constructor")

    def __init__(self, x):
        print("one arg constructor")

    def __init__(self, x, y):
        print("two arg constructor")


# t = Test()  # TypeError: __init__() missing 2 required positional arguments: 'x' and 'y'
# t = Test(10)  # TypeError: __init__() missing 1 required positional argument: 'y'
t = Test(10, 20)  # two arg constructor
