"""
Abstract class:
---------------
Some times implementation of a class is not complete, such type of partially
implementation classes are called abstract classes. Every abstract class in Python should
be derived from ABC class which is present in abc module.
"""
# case 1:
from abc import *


class Test:
    pass


t = Test()


# In the above code we can create object for Test class bcz it is concrete class and it does not
# contain any abstract method.


# case 2:
class Test(ABC):
    pass


t1 = Test()


# In the above code we can create object, even it is derived from ABC class, bcz it does not
# contain any abstract method.


# case 3:
class Test:
    @abstractmethod
    def m1(self):
        pass


t2 = Test()
# We can create object even class contains abstract method bcz we are not extending ABC class.


# case 4:
class Test(ABC):
    @abstractmethod
    def m1(self):
        pass


# t3 = Test()  # TypeError: Can't instantiate abstract class Test with abstract methods m1

'''
Conclusion 1:
------------
If a class contains at least one abstract method and if we are extending ABC class then 
instantiation is not possible

"abstract class with abstract method instantiation is not possible"

Parent class abstract methods should be implemented in the child classes. Otherwise we
cannot instantiate child class. 
If we are not creating child class object then we won't get any error
'''


# case 5:
class Vehicle(ABC):

    @abstractmethod
    def wheels(self):
        pass


class Car(Vehicle):
    pass
# It is valid because we are not creating Child class object.


# case 6:
class Vehicle(ABC):

    @abstractmethod
    def wheels(self):
        pass


class Car(Vehicle):
    pass


# c = Car()  # TypeError: Can't instantiate abstract class Car with abstract methods wheels
'''
Note: 
If we are extending abstract class and does not override its abstract method then
child class is also abstract and instantiation is not possible.

Note: 
Abstract class can contain both abstract and non-abstract methods also.
'''


# case 7:
class Vehicle(ABC):

    @abstractmethod
    def wheels(self):
        pass

    @abstractmethod
    def color(self):
        pass


class Car(Vehicle):
    def wheels(self):
        print("car wheels are 4")


# c = Car()  # TypeError: Can't instantiate abstract class Car with abstract methods color
# NOTE: Child class didn't implemented color abstract method from Parent class


# case 8:
class Vehicle(ABC):

    @abstractmethod
    def wheels(self):
        pass

    @abstractmethod
    def color(self):
        pass


class Car(Vehicle):
    def wheels(self):
        print("car wheels are 4")

    def color(self):
        print("car color is grey")


c = Car()
c.wheels()  # car wheels are 4
c.color()  # car color is grey


# case 9:
class Vehicle(ABC):

    def wheels(self):
        pass

    @abstractmethod
    def color(self):
        pass


class Car(Vehicle):

    def color(self):
        print("car color is grey")


c = Car()
c.color()  # car color is grey


# case 10:
class Vehicle(ABC):

    @abstractmethod
    def wheels(self):
        pass


class Car(Vehicle):
    def wheels(self):
        return 4


class Auto(Vehicle):
    def wheels(self):
        return 3


c = Car()
print(c.wheels())  # 4
a = Auto()
print(a.wheels())  # 3
