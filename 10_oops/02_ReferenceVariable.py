"""
What is Reference Variable?
--------------------------
=>  The variable which can be used to refer object is called reference variable.
=>  By using reference variable, we can access properties and methods of object.
=>  By using reference variable, we can perform required operations on the object.
=>  An object can have multiple reference variable.

properties --> variables
methods --> functions
"""


class Student:
    """ This class is developed by Nav for reference variable demo purpose """

    # __init__(self) --> is a constructor
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

    # instance method
    def bio(self):
        print("Hi, my name is: ", self.name)
        print("My roll number is: ", self.roll_no)


# reference variables
s = Student("Tom", 1)
print(s.name)  # Tom
print(s.roll_no)  # 1
s.bio()

# s1 = Student(2, "John")   # this won't be an error but this approach is incorrect
s1 = Student("John", 2)
print(s1.name)  # John
print(s1.roll_no)  # 2
s1.bio()
