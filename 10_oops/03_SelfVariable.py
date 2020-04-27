"""
# self is the default variable which is always pointing to current object (like this keyword in Java)
# self variable is always pointing to current object
# By using self we can declare instance variables
# By using self we can access instance variable values
# By using self we can access instance methods of object.
# The first argument of the constructor and instance method must be self
# PVM is responsible to provide value for self argument
# self is not a keyword, instead of self we can use any name but recommended to use self
# we can't use self from outside the class
# The main objective of constructors is to declare and initialize instance variables
"""


# case 1:
class Test:

    def __init__(self):
        print("The address of object pointed by self: ", id(self))  # 54996944


t = Test()
print("The address of object pointed by t: ", id(t))  # 54996944


# case 2:
class Test:

    def __init__(self):
        print("constructor")

    def m1(self, x):
        print("Value of x: ", x)


t = Test()  # constructor
t.m1(10)  # Value of x: 10


# case 3:
class Employee:
    """ This class is developed by Nav for self variable demo purpose """

    def __init__(self, emp_name, emp_salary):
        self.emp_name = emp_name
        self.emp_salary = emp_salary

    def info(self):
        print("*" * 10)
        print("Employee Name: ", self.emp_name)
        print("Employee Salary: ", self.emp_salary)
        print("*" * 10)


e1 = Employee("Chris", 77777)
e1.info()
# **********
# Employee Name:  Chris
# Employee Salary:  77777
# **********

e2 = Employee("Mark", 999999)
e2.info()
# **********
# Employee Name:  Mark
# Employee Salary:  999999
# **********
