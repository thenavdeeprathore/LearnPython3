"""
IS-A{Inheritance} vs HAS-A{Composition} Relationship:
--------------------------
=>  If we want to extend existing functionality with some more extra functionality then we
    should go for IS-A Relationship / Inheritance
=>  If we don't want to extend and just we have to use existing functionality then we
    should go for HAS-A Relationship / Composition
=>  Eg: Employee class extends Person class Functionality But Employee class just uses Car
    functionality but not extending
"""
# Car ----> Has-A ----> Employee
# Person ----> Is-A ----> Employee


class Car:
    def __init__(self, name, model, color):
        self.name = name
        self.model = model
        self.color = color

    def getinfo(self):
        print('\tCar Name:{}\n\tModel:{}\n\tColor:{}'.format(self.name, self.model, self.color))


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat_drink(self):
        print('Eating Pizza and Drinking Beer')


class Employee(Person):
    def __init__(self, name, age, eno, esal, car):
        super().__init__(name, age)
        self.eno = eno
        self.esal = esal
        self.car = car

    def work(self):
        print('Coding Python Programs..')

    def emp_info(self):
        print('Employee Name:', self.name)
        print('Employee Age:', self.age)
        print('Employee Number:', self.eno)
        print('Employee Salary:', self.esal)
        print('Employee Car Information:')
        self.car.getinfo()  # Employee using Car Functionality


car = Car('Kia', 'Seltos', 'Grey')
e = Employee('John', 48, 872425, 10000, car)
e.eat_drink()  # Employee using Person class functionality
e.work()
e.emp_info()
# Eating Pizza and Drinking Beer
# Coding Python Programs..
# Employee Name: John
# Employee Age: 48
# Employee Number: 872425
# Employee Salary: 10000
# Employee Car Information:
# 	Car Name:Kia
# 	Model:Seltos
# 	Color:Grey
