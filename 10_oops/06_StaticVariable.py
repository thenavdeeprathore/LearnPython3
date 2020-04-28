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

How to delete static variables?
------------------------------
Either className or cls variable
"""


# case 1:
class Student:
    """ This class is developed by Nav for static variable demo purpose """
    college_name = 'Harvard'  # for all objects a single copy is maintained at class level

    def __init__(self, x, y):
        self.name = x
        self.roll_no = y


s1 = Student("Tom", 101)
s2 = Student("Jerry", 102)
print(s1.name, s1.roll_no, s1.college_name)  # Tom 101 Harvard
print(s2.name, s2.roll_no, s2.college_name)  # Jerry 102 Harvard


# case 2: How to Declare static variables
class Test:
    a = 10  # Within the class directly but from outside of any method

    def __init__(self):
        Test.b = 20  # Inside constructor by using class name

    def m1(self):
        Test.c = 30  # Inside instance method by using class name

    @classmethod
    def m2(cls):
        cls.d = 40  # Inside @classmethod by using cls variable
        Test.e = 50  # Inside @classmethod by using class name

    @staticmethod
    def m3():
        Test.f = 60  # Inside @staticmethod by using class name


Test.g = 70  # from outside the class by using class name
print(Test.__dict__)
t = Test()
print(Test.__dict__)


# case 3: How to access static variable
class Test:
    # Inside class: classname, self, cls
    a = 10

    def __init__(self):
        print("inside constructor")
        print(Test.a)  # 10
        print(self.a)  # 10

    def m1(self):
        print("inside instance method")
        print(Test.a)  # 10
        print(self.a)  # 10

    @classmethod
    def m2(cls):
        print("inside class method")
        print(Test.a)  # 10
        print(cls.a)  # 10

    @staticmethod
    def m3():
        print("inside static method")
        print(Test.a)  # 10


t1 = Test()
t1.m1()
t1.m2()
t1.m3()
# Outside class: object reference, classname
print("outside class")
print(Test.a)  # 10
print(t1.a)  # 10


# case 4: How to modify static variable
# inside class - classname, cls
# outside class - classname
class Test:
    a = 10

    def __init__(self):
        Test.a = 20

    def m1(self):
        Test.a = 30

    @classmethod
    def m2(cls):
        cls.a = 40
        Test.a = 50

    @staticmethod
    def m3():
        Test.a = 60


print("Modify static variables")
print(Test.a)  # 10
t2 = Test()
t2.m1()
t2.m2()
t2.m3()
print(t2.a)  # 60
t2.a = 70
print(t2.a)  # 70
print(Test.a)  # 60
Test.a = 80
print(Test.a)  # 80


# Q1) Find output
class Test:
    a = 10  # static variable

    def m1(self):
        self.a = 777  # instance variable


st = Test()
st.m1()
print(Test.a)  # 10
# By using object reference first priority goes for Instance variable
print(st.a)  # 777


# Q2) Find output
class Test:
    a = 10  # static variable

    def m1(self):
        Test.a = 777  # static variable


print(Test.a)  # 10
st1 = Test()
st1.m1()
print(Test.a)  # 777
# By using object reference first priority goes for Instance variable
# if Instance variable is not present then it will look for static variable
print(st1.a)  # 777


# Q3) Find output
class Test:
    a = 10  # static variable

    def __init__(self):
        self.b = 20


t1 = Test()
t2 = Test()
print("t1: ", t1.a, t1.b)  # t1:  10 20
print("t2: ", t2.a, t2.b)  # t2:  10 20
t1.a = 1000
t1.b = 2000
print("t1: ", t1.a, t1.b)  # t1:  1000 2000
print("t2: ", t2.a, t2.b)  # t2:  10 20
Test.a = 10000
Test.b = 20000
print("t1: ", t1.a, t1.b)  # t1:  1000 2000
print("t2: ", t2.a, t2.b)  # t2:  10000 20
print("Test: ", Test.a, Test.b)  # Test:  10000 20000


# Q4) Find output
class Test:
    a = 10  # static variable

    def __init__(self):
        self.b = 20  # instance variable


t1 = Test()
t2 = Test()
Test.a = 555  # a = 555
t1.b = 777  # t1 --> b = 777
print("t1: ", t1.a, t1.b)  # t1:  555 777
print("t2: ", t2.a, t2.b)  # t2:  555 20


# Q5) Find output
class Test:
    a = 10  # static variable

    def __init__(self):
        self.b = 20  # instance variable

    def m1(self):
        self.a = 30
        self.b = 40


t1 = Test()
t2 = Test()
t1.m1()
print("t1: ", t1.a, t1.b)  # t1:  30 40
print("t2: ", t2.a, t2.b)  # t2:  10 20


# Q6) Find output
class Test:
    a = 10  # static variable

    def __init__(self):
        self.b = 20  # instance variable

    def m1(self):
        self.a = 30
        self.b = 40


t1 = Test()
t2 = Test()
t1.m1()
t2.m1()
print("t1: ", t1.a, t1.b)  # t1:  30 40
print("t2: ", t2.a, t2.b)  # t2:  30 40


# Q7) Find output
class Test:
    a = 10  # static variable

    def __init__(self):
        self.b = 20  # instance variable

    @classmethod
    def m1(cls):
        cls.a = 333
        cls.b = 666


t1 = Test()
t2 = Test()
t1.m1()
print("t1: ", t1.a, t1.b)  # t1:  333 20
print("t2: ", t2.a, t2.b)  # t2:  333 20
print("Test: ", Test.a, Test.b)  # 333 666


# case 5: How to delete static variable
class Test:

    a = 10
    b = 20
    c = 30
    d = 40

    @classmethod
    def m1(cls):
        del cls.a
        del Test.b


print(Test.__dict__)  # {'a': 10, 'b': 20, 'c': 30, 'd': 40}
Test.m1()
print(Test.__dict__)  # {'c': 30, 'd': 40}
del Test.c
print(Test.__dict__)  # {'d': 40}


# Q8) Find output
class Test:

    a = 10

    def __init__(self):
        Test.b = 20
        del Test.a

    def m1(self):
        Test.c = 30
        del Test.b

    @classmethod
    def m2(cls):
        Test.d = 40
        del Test.c

    @staticmethod
    def m3():
        Test.e = 50
        del Test.d


print(Test.__dict__)  # {'a': 10}
dt = Test()
print(Test.__dict__)  # {'b': 20}
dt.m1()
print(Test.__dict__)  # {'c': 30}
dt.m2()
print(Test.__dict__)  # {'d': 40}
dt.m3()
print(Test.__dict__)  # {'e': 50}

'''
NOTE:
====
Declare static variables:       class name or cls variable
Access static variables:        class name or self variable or cls variable or object reference
Modify static variables:        class name or cls variable 
Delete Static Variables:        class name or cls variable
'''
