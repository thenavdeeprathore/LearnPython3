"""
Method Resolution Order (MRO) / C3 algorithm:
---------------------------------------------
=>  In Hybrid Inheritance the method resolution order is decided based on MRO algorithm.
=>  This algorithm is also known as C3 algorithm.
=>  Samuele Pedroni proposed this algorithm.
=>  It follows DLR (Depth First Left to Right) i.e Child will get more priority than Parent.
=>  Left Parent will get more priority than Right Parent.
=>  MRO(X) = X+Merge(MRO(P1),MRO(P2),...,ParentList)

Head Element vs Tail Terminology:
--------------------------------
=>  Assume C1,C2,C3,...are classes.
=>  In the list: C1C2C3C4C5....
=>  C1 is considered as Head Element and remaining is considered as Tail.

Note:   We can find MRO of any class by using mro() function.
        print(ClassName.mro())

mro(A) = A, object
mro(B) = B, A, object
mro(C) = C, A, object
mro(D) = D, B, C, A, object
"""


# case 1:
class A:
    def m1(self):
        print("A class method")


class B(A):
    def m1(self):
        print("B class method")


class C(A):
    def m1(self):
        print("C class method")


class D(B, C):
    pass


print(A.mro())  # [<class '__main__.A'>, <class 'object'>]
print(B.mro())  # [<class '__main__.B'>, <class '__main__.A'>, <class 'object'>]
print(C.mro())  # [<class '__main__.C'>, <class '__main__.A'>, <class 'object'>]
print(D.mro())
# [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]
d = D()  # DBCAO
d.m1()  # B class method


# case 2:
class A: pass


class B: pass


class C: pass


class X(A, B): pass


class Y(B, C): pass


class P(X, Y, C): pass


print(A.mro())  # AO
print(B.mro())  # BO
print(C.mro())  # CO
print(X.mro())  # XABO
print(Y.mro())  # YBCO
print(P.mro())  # PXAYBCO
