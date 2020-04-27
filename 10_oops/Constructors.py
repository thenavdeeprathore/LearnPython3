# constructor is a special method in python
# constructors are used to write the logic
# name of the constructor is always: __init__()
# constructor will be executed automatically at the time of object creation
# Main objective of constructor is: to declare and initialize instance variables
# at least one argument -- self
# constructor is not mandatory for every class, python will provide default constructor


# case 1: constructor will be executed once for every object creation
class Test1:

    def __init__(self):
        print("0-arg default constructor")


# Best Practise: To create objects with different names
obj1 = Test1()  # 0-arg default constructor
obj2 = Test1()  # 0-arg default constructor
obj3 = Test1()  # 0-arg default constructor


# case 2: overloading concept is not present in constructors
# It will always take the latest constructor
class Test2:

    def __init__(self):
        print("no-arg constructor")

    def __init__(self, x):
        print("one-arg constructor")


# obj4 = Test2()  # TypeError: __init__() missing 1 required positional argument: 'x'
obj5 = Test2(10)  # one-arg constructor
obj6 = Test2(20)  # one-arg constructor


# case 3: calling instance variable
class Test3:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        print(self.a + self.b)  # calling instance variable

    def mul(self):
        print(self.a * self.b)  # calling instance variable


obj = Test3(100, 200)
obj.add()
obj.mul()


# case 4: calling instance method
class Test4:

    def m1(self):
        print("method m1")
        self.m2(10)

    def m2(self, a):
        print("method m2", a)


t = Test4()
t.m1()


# case 5: constructor with arguments
class Test5:
    name = "john"

    def __init__(self, name):
        print("good morning", name)  # local variable
        print("good evening", self.name)  # instance variable


c = Test5("Tom")


# case 6: conversions of local var to class var
class Operations:

    def __init__(self, num1, num2):
        print(num1)  # local variable
        print(num2)  # local variable
        # MOST IMPORTANT: conversions of local var to class var
        self.num1 = num1  # instance variable
        self.num2 = num2  # instance variable

    def add(self):
        print(self.num1 + self.num2)

    def mul(self):
        print(self.num1 * self.num2)


o = Operations(10, 20)
o.add()
o.mul()


class Emp:

    def __init__(self, eid, ename, esal):
        self.eid = eid
        self.ename = ename
        self.esal = esal

    def disp(self):
        print("EmpId: {} Ename: {} Esal: {}".format(self.eid, self.ename, self.esal))


e = Emp(111, "Navdeep", 9999999)
e.disp()


# __str__
class test:
    def __str__(self):
        return "tom"  # if you don't write return statement then it will throw error


c = test()
print(c)


class Emp1:

    def __init__(self, eid, ename, esal):
        self.eid = eid
        self.ename = ename
        self.esal = esal

    def __str__(self):
        # print("EmpId: {} Ename: {} Esal: {}".format(self.eid, self.ename, self.esal))
        return "EmpId: {} Ename: {} Esal: {}".format(self.eid, self.ename, self.esal)  # return is important


e1 = Emp1(111, "Navdeep", 9999999)
print(e1)  # printing ref var -- internally it calls __str__()


# __del__()  : executed when we destroy objects
class des():
    def __del__(self):
        print("Object destroyed...")


d1 = des()
d2 = des()
del d1
del d2


class My1:
    def __del__(self):
        print("object destroyed........")


c1 = My1()
c2 = c1
c3 = c1

del c1
del c2
del c3
