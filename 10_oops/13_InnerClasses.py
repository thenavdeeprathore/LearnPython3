# How to access members of one class inside another class


class Employee:

    # constructor
    def __init__(self, emp_no, emp_name, emp_sal):
        self.emp_no = emp_no
        self.emp_name = emp_name
        self.emp_Sal = emp_sal

    # instance method
    def display(self):
        print("Employee Number: ", self.emp_no)
        print("Employee Name: ", self.emp_name)
        print("Employee Salary: ", self.emp_Sal)


class Test:

    @staticmethod
    def modify(emp):
        emp.emp_Sal = emp.emp_Sal + 10000
        emp.display()


e = Employee(667864, "Vicky", 70000)
Test.modify(e)
# Employee Number:  667864
# Employee Name:  Vicky
# Employee Salary:  80000


# Inner classes
"""
1) Class which is declared inside another class
2) Without existing one type of object if there is no chance of existing another type of object
   then we should go for inner classes


# Without car, engine can't exist
# Without university, departments can't exist
# Without existing outer class object there is no chance of existing inner class object
# Inner class object is always associated with outer class objects
# We can declare any number of inner classes
"""


# case 1:
class Outer:

    def __init__(self):
        print('Outer class constructor')

    def m2(self):
        print('Outer class method')

    class Inner:

        def __init__(self):
            print('Inner class constructor')

        def m1(self):
            print('Inner class method')


o = Outer()  # Outer class constructor
i = o.Inner()  # Inner class constructor
i.m1()  # Inner class method

i = Outer().Inner()
i.m1()
# Outer class constructor
# Inner class constructor
# Inner class method

Outer().Inner().m1()
# Outer class constructor
# Inner class constructor
# Inner class method

# Outer().Inner().m2()  # AttributeError: 'Inner' object has no attribute 'm2'


# case 2:
class Human:

    def __init__(self, name):
        self.name = name
        self.head = self.Head()
        self.brain = self.head.Brain()

    def display(self):
        print("Hello..", self.name)

    class Head:
        def talk(self):
            print('Talking...')

        class Brain:
            def think(self):
                print('Thinking...')


h = Human("vicky")
h.display()  # Hello.. vicky
h.head.talk()  # Talking...
h.brain.think()  # Thinking...


# case 3:
class Person:

    def __init__(self):
        self.name = "Vicky"
        self.dob = self.DOB()

    def display(self):
        print("Name: ", self.name)
        self.dob.display()

    class DOB:

        def __init__(self):
            self.dd = 11
            self.mm = 8
            self.yy = 1990

        def display(self):
            print("Date of Birth = {}/{}/{} ".format(self.dd, self.mm, self.yy))


p = Person()
p.display()
# Name:  Vicky
# Date of Birth = 11/8/1990
