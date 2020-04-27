# class is a logical entity contains logic of the application
# class is a blueprint, it decides object creation

# object is a physical entity which represent memory

"""
Python 2.7: our class is not child class of object
class MyClass:
    pass

class MyClass():
    pass


Python 3.x: our class is child class of object
"""


# case 1: class is child class of object
class Class1:
    pass


class Class2():
    pass


class Class3(object):
    pass


print(issubclass(Class1, object))
print(issubclass(Class2, object))
print(issubclass(Class3, object))


# case 2: self variable is important for functions inside the class
class Class4:

    def disp1(self):  # self is important for functions inside the class
        print("good morning")

    def disp2(self, name):
        print("good evening", name)


c = Class4()
c.disp1()
c.disp2("Navdeep")


# case 3: instance and static method
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

# case 4: Declaring local, global and instance variables inside the class
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

# case 5: Declaring local, global and instance variables inside the class with the same names
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


# case 6: for single class you can create multiple objects
class Test3:
    def m1(self):
        print("good morning")


obj1 = Test3()
obj1.m1()

obj2 = Test3()
obj2.m1()


# case 7: objects can be created in two ways:
# named objects         obj = Myclass()
# name less objects     Myclass()
class Test4:
    def m1(self):
        print("good evening")


Test4().m1()  # name less objects


# case 8: memory of objects
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


# case 9: different objects actions
class Abc:
    name = "John"


c1 = Abc()
print(c1.name)  # John
c1.name = "Mike"
print(c1.name)  # Mike

c2 = Abc()
print(c2.name)  # John
