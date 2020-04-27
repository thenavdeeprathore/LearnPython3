"""
# constructor is a special method in python
# constructors are used to write the logic
# name of the constructor is always: __init__(self)
# constructor will be executed automatically at the time of object creation
# Main objective of constructor is: to declare and initialize instance variables
# Constructor can take at least one argument(at least self)
# constructor is not mandatory for every class, python will provide default constructor
"""


# case 1: constructor will be executed once for every object creation
class Test1:

    def __init__(self):
        print("no-arg constructor")


# Best Practise: To create objects with different names
obj1 = Test1()  # no-arg constructor
obj2 = Test1()  # no-arg constructor
obj3 = Test1()  # no-arg constructor


# case 2: default constructor
class Test:

    def m1(self):
        print("m1 method")


o1 = Test()  #
o2 = Test()  #
o3 = Test()  #


# case 3: calling constructor from outside the class after creating an object
class Test:

    def __init__(self):
        print("0-arg constructor")


t = Test()  # no-arg constructor
t.__init__()  # no-arg constructor


# case 4: overloading concept is not present in constructors
# It will always take the latest constructor
class Test2:

    def __init__(self):
        print("no-arg constructor")

    def __init__(self, x):
        print("one-arg constructor")


# obj4 = Test2()  # TypeError: __init__() missing 1 required positional argument: 'x'
obj5 = Test2(10)  # one-arg constructor
obj6 = Test2(20)  # one-arg constructor


# case 5: calling instance variable
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


# case 6: calling instance method
class Test4:

    def m1(self):
        print("method m1")
        self.m2(10)

    def m2(self, a):
        print("method m2", a)


t = Test4()
t.m1()


# case 7: constructor with arguments
class Test5:
    name = "john"

    def __init__(self, name):
        print("good morning", name)  # local variable
        print("good evening", self.name)  # instance variable


c = Test5("Tom")


# case 8: conversions of local var to class var
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
