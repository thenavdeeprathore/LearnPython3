"""
What is Class:
--------------
=>  In Python every thing is an object. To create objects we required some Model or Plan
    or Blue print, which is nothing but class.
=>  We can write a class to represent properties (attributes) and actions (behaviour) of object.
=>  Properties can be represented by variables
=>  Actions can be represented by Methods.
=>  Hence class contains both variables and methods

# class is a logical entity which contains logic of the application
# class is a blueprint, it decides object creation
# object is a physical entity which represent memory

How to define a Class?
----------------------
=>  We can define a class by using class keyword.
=>  Syntax:
        class className:
        ''' documenttation string '''
        variables: instance variables, static and local variables
        methods: instance methods, static methods, class methods

Documentation string represents description of the class. Within the class doc string is
always optional. We can get doc string by using the following 2 ways.

1) print(classname.__doc__)
2) help(classname)

Python 2.7: our class is not child class of object
class MyClass:
    pass

class MyClass():
    pass


Python 3.x: our class is child class of object


What is Object:
--------------
=>  Physical existence of a class is nothing but object.
=>  We can create any number of objects for a class.
=>  Syntax to Create Object: referencevariable = classname()
=>  Example: s = Student()
"""


# case 1:
class Student:
    """ This is a student class with required data """


print(Student.__doc__)
# This is a student class with required data
help(Student)
# Help on class Student in module __main__:
#
# class Student(builtins.object)
#  |  This is a student class with required data
#  |
#  |  Data descriptors defined here:
#  |
#  |  __dict__
#  |      dictionary for instance variables (if defined)
#  |
#  |  __weakref__
#  |      list of weak references to the object (if defined)


# case 2: Different ways to declare a class which is child class of object
class Class1:
    pass


class Class2():
    pass


class Class3(object):
    pass


print(issubclass(Class1, object))
print(issubclass(Class2, object))
print(issubclass(Class3, object))


# case 3: self variable is important for functions inside the class
class Class4:

    def disp1(self):  # self is important for functions inside the class
        print("good morning")

    def disp2(self, name):
        print("good evening", name)


c = Class4()
c.disp1()
c.disp2("Navdeep")


# case 4: instance and static method
class Class5:

    def m1(self):
        print("instance method")

    @staticmethod
    def m2():
        print("static method")


c = Class5()
c.m1()
c.m2()

# Class5.m1() # TypeError: m1() missing 1 required positional argument: 'self'
Class5.m2()


# case 5: Declaring local, global and instance variables inside the class
i, j = 100, 200  # global var


class Test1:
    a, b = 10, 20  # class var/instance variable

    def add(self, x, y):  # local var
        print(x + y)
        print(self.a + self.b)
        print(i + j)

    def mul(self, x, y):
        print(x * y)
        print(self.a * self.b)
        print(i * j)


c = Test1()
c.add(1000, 2000)
c.mul(1000, 2000)


# case 6: Declaring local, global and instance variables inside the class with the same names
a, b = 100, 200  # global var


class Test2:
    a, b = 10, 20  # class var

    def add(self, a, b):  # local var
        print(a + b)
        print(self.a + self.b)
        print(globals()['a'] + globals()['b'])

    def mul(self, x, y):
        print("Local: ", a * b)
        print("Instance: ", self.a * self.b)
        print("Global: ", globals()['a'] * globals()['b'])


c = Test2()
c.add(1000, 2000)
c.mul(1000, 2000)


# case 7: for single class you can create multiple objects
class Test3:
    def m1(self):
        print("good morning")


obj1 = Test3()
obj1.m1()

obj2 = Test3()
obj2.m1()


# case 8: objects can be created in two ways:
# named objects         obj = Myclass()
# name less objects     Myclass()
class Test4:
    def m1(self):
        print("good evening")


Test4().m1()  # name less objects


# case 9: memory of objects
class Nav:
    pass


c1 = Nav()
c2 = Nav()
c3 = c1
print(id(c1))
print(id(c2))
print(id(c3))

print(c1 is c2)  # False
print(c1 is c3)  # True


# case 10: different objects actions
class Abc:
    name = "John"


c1 = Abc()
print(c1.name)  # John
c1.name = "Mike"
print(c1.name)  # Mike

c2 = Abc()
print(c2.name)  # John
