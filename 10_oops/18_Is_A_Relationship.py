"""
2) By Inheritance (IS-A Relationship):
-------------------------------------
What ever variables, methods and constructors available in the parent class by default
available to the child classes and we are not required to rewrite.

Hence the main advantage of inheritance is
    - Code Re-usability and we can
    - extend existing functionality with some more extra functionality.
"""


# case 1:
class P:
    a = 10  # static variable

    def __init__(self):
        print("Parent constructor")
        self.b = 20  # instance variable

    def m1(self):
        print("Parent instance method")

    @classmethod
    def m2(cls):
        print("Parent class method")

    @staticmethod
    def m3():
        print("Parent static method")


class C(P):
    pass


c = C()  # Parent constructor
print(c.a)  # 10
print(c.b)  # 20
c.m1()  # Parent instance method
c.m2()  # Parent class method
c.m3()  # Parent static method


# case 2:
# Note: What ever members present in Parent class are by default available to the child
# class through inheritance.
class Parent:

    def m1(self):
        print("Parent class method")


class Child(Parent):

    def m2(self):
        print("Child class method")


p = Parent()
p.m1()  # Parent class method
# p.m2()  # AttributeError: 'Parent' object has no attribute 'm2'
c = Child()
c.m1()  # Parent class method
c.m2()  # Child class method


# case 3:
class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat_drink(self):
        print("Eat Pizza Drink Beer")


class Employee(Person):

    def __init__(self, name, age, emp_no, emp_sal):
        super().__init__(name, age)
        self.emp_no = emp_no
        self.emp_sal = emp_sal

    def work(self):
        print("Coding python is very easy")

    def emp_info(self):
        print("Employee Name:", self.name)
        print("Employee Age:", self.age)
        print("Employee Number:", self.emp_no)
        print("Employee Salary:", self.emp_sal)


e = Employee("noddy", 23, 1234, 10000000)
e.eat_drink()  # Eat Pizza Drink Beer
e.work()  # Coding python is very easy
e.emp_info()
# Employee Name: noddy
# Employee Age: 23
# Employee Number: 1234
# Employee Salary: 10000000
