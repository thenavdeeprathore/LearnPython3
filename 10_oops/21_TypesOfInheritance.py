"""
Inheritance -- Code re-usability and extension of the functionality

Types of Inheritance:
--------------------
1) Single
2) Multi level
3) Hierarchical
4) Multiple {In java Multiple Inheritance is not allowed}
5) Hybrid
6) Cyclic {Not supported by Python}
"""


# Inheritance
class Parent:

    def property(self):
        print('cash + land + gold')

    def marriage(self):
        print('Minnie')


class Child(Parent):

    def marriage(self):
        super().marriage()  # Minnie
        print('Katrina')  # Katrina


c = Child()
c.property()
c.marriage()


# 1) Single Inheritance
# Single Parent and Single Child
# The concept of inheriting the properties from one class to another class
class Parent1:
    def m1(self):
        print("parent method")


class Child1(Parent1):
    def m2(self):
        print("child method")


p = Parent1()
p.m1()

c = Child1()
c.m1()
c.m2()


# 2) Multi level Inheritance
# Grandparent --> Parent --> Child
# The concept of inheriting the properties from multiple classes to single class with the
# concept of one after another is known as multi level inheritance.
class A:
    def m1(self):
        print("A method")


class B(A):
    def m2(self):
        print("B method")


class C(B):
    def m3(self):
        print("C method")


c = C()
c.m1()
c.m2()
c.m3()


# 3) Hierarchical Inheritance
# one parent but multiple child classes and all child classes at the same level
# The concept of inheriting properties from one class into multiple classes which are
# present at same level is known as Hierarchical Inheritance
class P:
    def m1(self):
        print("Parent method")


class C1(P):
    def m2(self):
        print("c1 method")


class C2(P):
    def m3(self):
        print("c2 method")


c = C1()
c.m1()
c.m2()

c1 = C2()
c1.m1()
c1.m3()


# 4) Multiple Inheritance:
# Multiple Parents but Single Child
# The concept of inheriting the properties from multiple classes into a single class at a
# time, is known as multiple inheritance.

# If the same method is inherited from both parent classes, then Python will always
# consider the order of Parent classes in the declaration of the child class.
# class C(P1, P2):  P1 method will be considered
# class C(P2, P1):  P2 method will be considered
class P1:
    def m1(self):
        print("Parent1 method")


class P2:
    def m2(self):
        print("Parent2 method")


class C(P1, P2):

    def m3(self):
        print("Child method")


c = C()
c.m1()  # Parent1 method
c.m2()  # Parent2 method
c.m3()  # Child method


# 5) Hybrid Inheritance:
# Combination of Single, Multi level, multiple and Hierarchical inheritance is known as
# Hybrid Inheritance.
# In Hybrid Inheritance the method resolution order is decided based on MRO algorithm.

# 6) Cyclic Inheritance: {Not supported by Python}
# Parent and child are both same class
# The concept of inheriting properties from one class to another class in cyclic way, is
# called Cyclic inheritance. Python won't support for Cyclic Inheritance
# case 1:
class A(A):
    pass


# case 2:
class A(B):
    pass


class B(A):
    pass
