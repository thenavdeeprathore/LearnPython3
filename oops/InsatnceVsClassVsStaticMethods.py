# Difference between Instance method vs Class method

"""
# 1) Inside method body if we are using atleast one instance variable then
# compulsory we should declare that method as instance method
# 1) Inside method body if we are using only static variables then
# it is highly recommended to declare that method as class method

# 2) Instance method doesn't required any decorator
# 2) Class method requires decorator @classmethod

# 3) First argument in Instance method should be self
# 3) First argument in Class method should be cls

# 4) Inside Instance method -- we can access both instance and static variables
# 4) Inside class method -- we can access only static variables

# 5) Instance method -- we can call by using object reference
# 5) Class method -- we can call by both object reference and classname
"""


# case 1: class method

class Animal:
    legs = 4

    @classmethod
    def walk(cls, name):
        print('{} walks with {} legs'.format(name, cls.legs))
        # print('{} walks with {} legs'.format(name, Animal.legs))


Animal.walk("Dog")
Animal.walk("Cat")


# case 2: class method - Count number of objects created for a class
class Test:
    count = 0

    def __init__(self):
        Test.count = Test.count + 1

    @classmethod
    def getNoOfObjects(cls):
        print("The number of objects created: ", cls.count)


t1 = Test()
t2 = Test()
t3 = Test()
Test.getNoOfObjects()


# static method
# general utility methods / helper methods

class Test:

    @staticmethod
    def sum(x, y):
        print('sum is: ', x + y)


Test.sum(10, 20)

# instance vs class vs static method:
"""
1. Instance Method : If we are using any instance variable inside method body
    1.1. We can call by object reference
2. Class Method : If we are using only static variables inside method body
    2.1. We can call by object reference or class name
3. Static Method : If we are not using both Instance and Static variable inside method body
    3.1. We can call by object reference or class name but recommended to use class name
"""

# If we are not using any decorator
"""
For class method, @classmethod decorator is mandatory 
For static method, @staticmethod decorator is optional

Without any decorator the method can be either instance method or static method
- If we are calling by using object reference then it should be Instance method
- If we are calling by using class name then it should be static method
"""


# case 1 : Invalid code
class Test:

    def m1():
        print('some method calling by using object reference')


t = Test()


# t.m1()  # object reference means calling instance method but self is not present


# case 2 : Valid code and Python will consider this method as static method
class Test:

    def m1():
        print('some method calling by using class name')


Test.m1()


# case 3 : Valid code
class Test:

    @staticmethod
    def m1():
        print('static method calling by using object reference and class name')


t = Test()
t.m1()
Test.m1()


# case 4 : Invalid code
class Test:

    def m1(x):  # TypeError: m1() takes 1 positional argument but 2 were given
        print('some method calling by using object reference', x)


t = Test()
t.m1(10)

# Note: Python will provide one argument self and one value x user is providing
