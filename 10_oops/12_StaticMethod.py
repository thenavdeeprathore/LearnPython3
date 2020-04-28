"""
3) Static Methods:
-----------------
=>  In general these methods are general utility methods.
=>  Inside these methods we won't use any instance or class variables.
=>  Here we won't provide self or cls arguments at the time of declaration.
=>  We can declare static method explicitly by using @staticmethod decorator
=>  We can access static methods by using class name or object reference

Note:
-----
-   In general we can use only instance and static methods. Inside static method we can
    access class level variables by using class name.
-   Class methods are most rarely used methods in python.
"""


class Calculator:

    @staticmethod
    def add(a, b):
        print(f"The sum is {a + b}")

    @staticmethod
    def product(a, b):
        print(f"The multiplication is: {a * b}")

    @staticmethod
    def average(a, b):
        print(f"The average is {(a + b)/2}")


Calculator.add(10, 20)  # The sum is 30
Calculator.product(10, 20)  # The multiplication is: 200
Calculator.average(10, 20)  # The average is 15.0


'''
Inside method --> at least one instance variable --> Instance Method
Inside method --> if we are not using instance variable but using static variable --> Class Method
Inside method --> if we are not using both instance and static variable --> Static Method

Inside instance method, we can access both instance and static variables
Inside class method, we can access only static variables
Inside static method, we can't access both instance and static variables

We can call instance method by using object reference
We can call class method either by using object reference or by using class name{recommended}
We can call static method either by using object reference or by using class name{recommended}
'''

"""
1) If we are using only instance variable --> Instance Method
2) If we are using only static variables --> Class Method
3) If we are using instance and static variables --> Instance Method
4) If we are using instance and local variables --> Instance Method
5) If we are using static and local variables --> Class Method
6) If we are using local variables --> Static Method
"""


# If we are not using any decorator for a method?
# @classmethod decorator is mandatory for class method
# @staticmethod decorator is optional for static method
'''
If you have a method without a decorator then it can be instance method or static method

- If you are calling by using object reference then it is Instance method
- If you are calling by class name then it is Static method
'''


# case 1:
class Dec:

    def m1():
        print("m1 method")


# Instance Method
# d = Dec()
# d.m1()  # TypeError: m1() takes 0 positional arguments but 1 was given

# Static Method
Dec.m1()  # m1 method


# case 2:
class Dec:

    def m2(x):
        print("m2 method")


# Instance Method
d = Dec()
d.m2()  # m2 method
# Static Method
# Dec.m2()  # TypeError: m2() missing 1 required positional argument: 'x'


# case 3:
class Dec:

    def m3(x):
        print("m3 method")


# Static Method
Dec.m3(10)  # m3 method
