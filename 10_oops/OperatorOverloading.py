# Polymorphism

"""
1) What is polymorphism
2) Duck typing philosophy of Python
3) Overloading
    - Operator overloading {supports by Python}
    - Methods overloading  {Doesn't support by Python}
    - Constructors overloading {Doesn't support by Python}
4) Overriding
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

print(10*3)
print("Hello"*3)


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

