"""
Setter and Getter Methods:
-------------------------
We can set and get the values of instance variables by using getter and setter methods.

Setter Method:
-------------
setter methods can be used to set values to the instance variables. setter methods also
known as mutator methods.

Syntax:
------
def setVariable(self,variable):
    self.variable=variable

Getter Method:
-------------
Getter methods can be used to get values of the instance variables. Getter methods also
known as accessor methods.

Syntax:
------
def getVariable(self):
    return self.variable
"""


class Student:

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_marks(self, mark):
        self.mark = mark

    def get_marks(self):
        return self.mark


n = int(input("Enter number of student: "))
for i in range(n):
    s = Student()
    name = input("Enter Name: ")
    s.set_name(name)
    marks = int(input("Enter Marks: "))
    s.set_marks(marks)
    print("Hi", s.get_name())
    print("Your marks are: ", s.get_marks())
