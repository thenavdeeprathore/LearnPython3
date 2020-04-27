class Book:

    def __init__(self, pages):
        self.pages = pages

    def __str__(self):  # overriding
        return 'The number of pages: ' + str(self.pages)

    # def __add__(self, other):
    #     return self.pages + other.pages

    def __add__(self, other):  # overloading
        total = self.pages + other.pages
        b = Book(total)
        return b


b1 = Book(100)
b2 = Book(200)
b3 = Book(300)
print(b1)
print(b2)
print(b3)
print(b1 + b2)
print(b1 + b2 + b3)
print(type(b1 + b2 + b3))  # <class '__main__.Book'>


# Whenever we are calling + operator then __add__() method will be called
# + operator return type will become __add__() method return type

# Whenever we are printing object reference then __str__() method will be called
# If we are not providing __str__() method then default implementation will be executed

class Book:

    def __init__(self, pages):
        self.pages = pages

    def __add__(self, other):  # overloading
        total = self.pages + other.pages
        b = Book(total)
        return b


b1 = Book(100)
print(b1)  # <__main__.Book object at 0x00AEC1A8>


class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __lt__(self, other):  # overload
        return self.marks < other.marks


s1 = Student("Vicky", 100)
s2 = Student("Rocky", 200)
print(s1 < s2)
print(s2 < s1)


class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __mul__(self, other):
        return self.salary * other.days


class Timesheet:

    def __init__(self, name, days):
        self.name = name
        self.days = days

    def __mul__(self, other):
        return self.days * other.salary


e = Employee('Vicky', 500)
t = Timesheet('Vicky', 25)
print('This month salary', e * t)
print('This month salary', t * e)
