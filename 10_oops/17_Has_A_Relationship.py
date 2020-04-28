"""
Using Members of One Class inside Another Class:
------------------------------------------------
We can use members of one class inside another class by using the following ways
1) By Composition (Has-A Relationship)
2) By Inheritance (IS-A Relationship)


1) By Composition (Has-A Relationship):
---------------------------------------
=>  By using Class Name or by creating object we can access members of one class inside
    another class is nothing but composition (Has-A Relationship).
=>  The main advantage of Has-A Relationship is Code Re-usability.
"""


# case 1: class Car Has-A Engine reference
class Engine:
    a = 10

    def __init__(self):
        self.b = 20

    def m1(self):
        print("engine functionality")


class Car:

    def __init__(self):
        self.engine = Engine()

    def m2(self):
        print("Car using engine functionality")
        print(self.engine.a)
        print(self.engine.b)
        self.engine.m1()


c = Car()
c.m2()


# Car using engine functionality
# 10
# 20
# engine functionality


# case 2:
class Car:

    def __init__(self, name, model, color):
        self.name = name
        self.model = model
        self.color = color

    def car_info(self):
        print(f"Car name: {self.name} , Car model: {self.model} , Car color: {self.color}")


class Employee:

    def __init__(self, emp_name, emp_no, emp_car):
        self.emp_name = emp_name
        self.emp_no = emp_no
        self.emp_car = emp_car

    def emp_car_info(self):
        print("Employee Name: ", self.emp_name)
        print("Employee Number: ", self.emp_no)
        print("Employee Car Info: ")
        self.emp_car.car_info()


c = Car("Kia", "Seltos", "Grey")
e = Employee("Vicky", "7777", c)
e.emp_car_info()

# Employee Name:  Vicky
# Employee Number:  7777
# Employee Car Info:
# Car name: Kia , Car model: Seltos , Car color: Grey


# case 3:
class SportsNews:

    def sports_info(self):
        print("sports information")


class MovieNews:

    def movies_info(self):
        print("movie information")


class CoronaVirusNews:

    def corona_info(self):
        print("Corona virus information")


class MyNews:

    def __init__(self):
        self.sports = SportsNews()
        self.movies = MovieNews()
        self.corona = CoronaVirusNews()

    def my_news_info(self):
        self.sports.sports_info()
        self.movies.movies_info()
        self.corona.corona_info()


m = MyNews()
m.my_news_info()
# sports information
# movie information
# Corona virus information


class TotalNews:

    def __init__(self, s, m, c):
        self.sports = s
        self.movies = m
        self.corona = c

    def my_news_info(self):
        self.sports.sports_info()
        self.movies.movies_info()
        self.corona.corona_info()


s = SportsNews()
m = MovieNews()
c = CoronaVirusNews()
t = TotalNews(s, m, c)
t.my_news_info()
# sports information
# movie information
# Corona virus information
