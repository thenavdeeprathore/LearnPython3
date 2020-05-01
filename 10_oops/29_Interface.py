"""
Interfaces In Python:
---------------------
In general if an abstract class contains only abstract methods then such type of abstract class is
considered as interface.

Purpose: acts as requirement specification
If we don't know anything about implementation just we have requirement specification then
we should go for interface.
"""
from abc import *


# case 1: interface
class Test(ABC):

    @abstractmethod
    def m1(self):
        print("m1 method")

    @abstractmethod
    def m2(self):
        print("m2 method")


# t = Test()  # TypeError: Can't instantiate abstract class Test with abstract methods m1, m2


# case 2: abstract class
class Test(ABC):

    def m1(self):
        print("m1 method")

    @abstractmethod
    def m2(self):
        print("m2 method")


# t = Test()  # TypeError: Can't instantiate abstract class Test with abstract methods m2


# case 3: concrete class
class Test(ABC):

    def m1(self):
        print("m1 method")

    def m2(self):
        print("m2 method")


t = Test()


'''
Concrete class vs Abstract Class vs Interface:
----------------------------------------------
1)  If we don't know anything about implementation just we have requirement
    specification then we should go for interface.
2)  If we are talking about implementation but not completely then we should go for
    abstract class. (partially implemented class).
3)  If we are talking about implementation completely and ready to provide service then
    we should go for concrete class.
'''


class InterfaceClass(ABC):
    @abstractmethod
    def m1(self): pass

    @abstractmethod
    def m2(self): pass

    @abstractmethod
    def m3(self): pass


class AbstractClass(InterfaceClass):
    def m1(self):
        print("m1 method implementation")

    def m2(self):
        print("m2 method implementation")


class ConcreteClass(AbstractClass):
    def m3(self):
        print("m3 method implementation")


c = ConcreteClass()
c.m1()  # m1 method implementation
c.m2()  # m2 method implementation
c.m3()  # m3 method implementation
