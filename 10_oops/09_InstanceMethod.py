"""
1) Instance Methods:
------------------
=>  Inside method implementation if we are using instance variables then such type of
    methods are called instance methods.
=>  Inside instance method declaration, we have to pass self variable. def m1(self):
=>  By using self variable inside method we can able to access instance variables.
=>  Within the class we can call instance method by using self variable and from outside of
    the class we can call by using object reference.
"""


class Test:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def m1(self, marks):
        print(f"Hi {self.name}")  # Hi John
        print(f"Your age is {self.age}")  # Your age is 23
        print(f"{self.name} your marks are {marks}")  # John your marks are 99


t = Test("John", 23)
t.m1(99)
