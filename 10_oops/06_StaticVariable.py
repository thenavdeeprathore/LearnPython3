"""
static variable : for all objects a single copy is maintained at class level

Declare static variables?
------------------------
# Within the class directly but from outside of any method
# Inside constructor by using class name
# Inside instance method by using class name
# Inside @classmethod by using cls variable or class name
# Inside @staticmethod by using class name
# from outside the class by using class name

How to access static variables?
------------------------------
# we can access either using classname or object reference
# Inside class: classname, self, cls
# Outside class: object reference, classname

# within the class we can access by using classname
# Inside classmethod we can also access using cls variable
# from outside the class by using class name
"""


class Student:
    """ This class is developed by Nav for static variable demo purpose """
    college_name = 'Harvard'

    def __init__(self, x, y):
        self.name = x
        self.roll_no = y


s1 = Student("Tom", 101)
s2 = Student("Jerry", 102)
print(s1.name, s1.roll_no, s1.college_name)
print(s2.name, s2.roll_no, s2.college_name)


# Declare static variables
class Test:
    a = 10

    def __init__(self):
        Test.b = 20

    def m1(self):
        Test.c = 30

    @classmethod
    def m2(cls):
        cls.d = 40
        Test.e = 50

    @staticmethod
    def m3():
        Test.f = 60


Test.g = 70
print(Test.__dict__)
t = Test()
print(Test.__dict__)


# access static variable
class Test:
    a = 10

    def __init__(self):
        print("inside constructor")
        print(Test.a)
        print(self.a)

    def m1(self):
        print("inside instance method")
        print(Test.a)
        print(self.a)

    @classmethod
    def m2(cls):
        print("inside class method")
        print(Test.a)
        print(cls.a)

    @staticmethod
    def m3():
        print("inside static method")
        print(Test.a)


t = Test()
t.m1()
t.m2()
t.m3()

print("outside class")
print(Test.a)
print(t.a)


# How to modify static variable
# inside class - classname, cls
# outside class - classname


class Test:
    a = 10

    def __init__(self):
        Test.a = 20

    @classmethod
    def m1(cls):
        cls.a = 30
        Test.a = 40

    @staticmethod
    def m2():
        Test.a = 50


t = Test()
t.m1()
t.m2()
t.a = 60
print(Test.a)  # 50
print(t.a)  # 60


# How to delete static variable
class Test:

    a = 1000

    def __init__(self):
        del Test.a


t = Test()
print(Test.a)
