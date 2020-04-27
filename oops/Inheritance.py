# Inheritance -- Code reusability and extension of the functionality
"""
-------------------
class P
    10 methods
class C(P)
    5 methods
--------------------
class P1
class P2
class P3

class C(P1, P2, P3)
    5 methods
"""


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


# Is-A vs Has-A relationship
# Aggregation and Composition
# Composition -- Strong association
# Aggregation -- Weak association


# Types of Inheritance:
"""
Single
Multi level
Hierarchical
Multiple {In java Multiple Inheritance is not allowed}
Hybrid
"""

# Single Inheritance
# Single Parent class
# Single Child class


class Parent:
    def m1(self):
        print("parent method")


class Child(Parent):
    def m2(self):
        print("child method")


p = Parent()
p.m1()

c = Child()
c.m1()
c.m2()


# Multi-level Inheritance
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


# Multiple Inheritance  - one child class with multiple parents class
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
