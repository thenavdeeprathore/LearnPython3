# self variable is similar like this keyword in java
# self variable is always pointing to current object
# The first argument of the constructor and instance method must be self
# PVM is responsible to provide value for self argument
# By using self we can declare instance variables
# By using self we can access instance variable values
# instead of self we can use any name but recommended to use self
# The main objective of constructors is to declare and initialize instance variables


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

e2 = Employee("Mark", 999999)
e2.info()
