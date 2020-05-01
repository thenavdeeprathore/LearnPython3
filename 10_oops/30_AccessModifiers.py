"""
Public, Protected and Private Attributes:
----------------------------------------

By default every attribute is public. We can access from anywhere either within the class
or from outside of the class.
Eg: name = 'john'

Protected attributes can be accessed within the class anywhere but from outside of the
class only in child classes.
We can specify an attribute as protected by prefixing with _symbol.
Syntax: _variablename = value
Eg: _name='john'
But is is just convention and in reality does not exists protected attributes

private attributes can be accessed only within the class. i.e from outside of the class we
cannot access. We can declare a variable as private explicitly by prefixing with 2
underscore symbols
syntax: __variablename=value
Eg: __name='john'
"""


# public {var = 10}
class Test:
    a = 10

    def __init__(self):
        print(Test.a)  # 10
        print(self.a)  # 10
        self.b = 20

    def m1(self):
        print("public method")  # public method

    def m2(self):
        print(Test.a)  # 10
        print(self.a)  # 10
        print(self.b)  # 20
        self.m1()  # public method


t = Test()
t.m1()
t.m2()
print(Test.a)  # 10
print(t.a)  # 10
print(t.b)  # 20


# private {__var = 10}
class Test1:

    __i = 100

    def __init__(self):
        self.__j = 200

    def __m1(self):
        print("private method")

    def m2(self):
        print(self.__i)  # 100
        print(self.__j)  # 200
        self.__m1()  # private method


t = Test1()
t.m2()
# print(Test1.__i)  # AttributeError: type object 'Test1' has no attribute '__i'
# print(t.__j)  # AttributeError: 'Test1' object has no attribute '__j'
# t.__m1()  # AttributeError: 'Test1' object has no attribute '__m1'


# How to Access Private Variables from Outside of the Class:
'''
We cannot access private variables directly from outside of the class.
But we can access indirectly as follows objectreference._classname__variablename
'''


class Test:

    def __init__(self):
        self.__x = 777

    def __m1(self):
        print("private method")


t = Test()
# Name mangling
print(t._Test__x)  # 777
t._Test__m1()  # private method


# protected {_x = 10}
class Test2:

    def __init__(self):
        self._a = 1000

    def m1(self):
        print(self._a)


class SubTest(Test2):

    def m2(self):
        print(self._a)


t = SubTest()
t.m1()  # 1000
t.m2()  # 1000
print(t._a)  # 1000 Strictly not implemented, just a naming conventions
