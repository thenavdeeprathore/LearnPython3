"""
super() Method:
--------------
super() is a built-in method which is useful to call the super class
constructors,
variables
and methods
from the child class.

If the parent class and child class contains a member with the same name then we should use super()
"""


# case 1:
class P:

    def m1(self):
        print('Parent m1 method')


class C(P):

    def m2(self):
        self.m1()
        print('Child m2 method')


c = C()
c.m2()
# Parent m1 method
# Child m2 method


# case 2: constructors, methods, variables
class Parent:

    a = 10

    def __init__(self):
        print("Parent constructor")

    def m1(self):
        print("Parent m1 instance method")

    @classmethod
    def m2(cls):
        print("Parent m2 class method")

    @staticmethod
    def m3():
        print("Parent m3 static method")

    def m4(self):
        print("Parent m4 method")


class Child(Parent):

    def __init__(self):
        print("Child constructor")

    def m4(self):
        print("Child m4 method")

    def display1(self):
        print("Child instance method")
        print(super().a)
        super().__init__()
        super().m1()
        super().m2()
        super().m3()

    def display2(self):
        print("Child instance method")
        print(self.a)
        super().__init__()  # same name
        self.m1()
        self.m2()
        self.m3()
        self.m4()  # priority will go to child method with the same name


c = Child()
c.display1()
# Child constructor
# Child instance method
# 10
# Parent constructor
# Parent m1 instance method
# Parent m2 class method
# Parent m3 static method
c.display2()
# Child constructor
# Child instance method
# 10
# Parent constructor
# Parent m1 instance method
# Parent m2 class method
# Parent m3 static method
# Child m4 method


# case 3: Parent and child class method with the same name
class A:
    def m1(self):
        print('A class method')


class B(A):
    def m1(self):
        print('B class method')


class C(B):
    def m1(self):
        print('C class method')


class D(C):
    def m1(self):
        print('D class method')


class E(D):
    def m1(self):
        # super()  # no output
        super().m1()  # D class method
        # NOTE: by using super() we can call immediate parent class methods.
        # If we want a particular super class method then we have 2 options:
        D.m1(self)  # D class method
        C.m1(self)  # C class method
        B.m1(self)  # B class method
        A.m1(self)  # A class method
        super(E, self).m1()  # D class method
        super(D, self).m1()  # C class method
        super(C, self).m1()  # B class method
        super(B, self).m1()  # A class method


e = E()
e.m1()


# super() vs instance variables
# NOTE: we can't use super() to access parent class instance variable
class P:

    a = 777  # static variable

    def __init__(self):
        self.b = 999  # instance variable


class C(P):

    def __init__(self):
        self.b = 100

    def m1(self):
        print(self.a)  # 777
        print(self.b)  # 100
        print(super().a)  # 777
        # print(super().b)  # AttributeError: 'super' object has no attribute 'b'


c = C()
c.m1()
# we can't access parent class instance variable from the child class using super()
# we can access using self variable


# Point 1:
# Child class --> constructor call using super()
class Parent1:

    def __init__(self):
        print("Parent constructor")

    def m1(self):
        print("Parent m1 instance method")

    @classmethod
    def m2(cls):
        print("Parent m2 class method")

    @staticmethod
    def m3():
        print("Parent m3 static method")


class Child1(Parent1):

    def __init__(self):
        print("***** Child constructor")
        super().__init__()  # Parent constructor
        super().m1()  # Parent m1 instance method
        super().m2()  # Parent m2 class method
        super().m3()  # Parent m3 static method

    def m1(self):
        print("***** Child instance method")
        super().__init__()  # Parent constructor
        super().m1()  # Parent m1 instance method
        super().m2()  # Parent m2 class method
        super().m3()  # Parent m3 static method

    @classmethod
    def m2(cls):
        print("***** Child class method")
        # super().__init__()  # TypeError: __init__() missing 1 required positional argument: 'self'
        # super().m1()  # TypeError: m1() missing 1 required positional argument: 'self'
        super(Child1, cls).__init__(cls)  # Parent constructor
        super(Child1, cls).m1(cls)  # Parent m1 instance method
        super().m2()  # Parent m2 class method
        super().m3()  # Parent m3 static method

    @staticmethod
    def m3():
        print("***** Child static method")
        # super().__init__()  # No way we can call this
        # super().m1()  # No way we can call this
        # super().m2()  # RuntimeError: super(): no arguments
        # super().m3()  # RuntimeError: super(): no arguments
        super(Child1, Child1).m2()  # Parent m2 class method
        super(Child1, Child1).m3()  # Parent m3 static method


c = Child1()
c.m1()
c.m2()
# c.m3()
Child1.m3()
