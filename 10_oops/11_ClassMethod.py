"""
2) Class Methods:
---------------
=>  Inside method implementation if we are using only class variables (static variables),
    then such type of methods we should declare as class method.
=>  We can declare class method explicitly by using @classmethod decorator.
=>  For class method we should provide cls variable at the time of declaration
=>  We can call classmethod by using class name or object reference variable.
"""


class Animal:

    legs = 4

    @classmethod
    def walk(cls, name):
        print(f"{name} walks with {cls.legs} legs")


Animal.walk("Dog")  # Dog walks with 4 legs
Animal.walk("Cat")  # Cat walks with 4 legs


class Test:

    count = 0

    def __init__(self):
        Test.count = Test.count + 1

    @classmethod
    def get_number_of_objects(cls):
        print(f"The number of objects created: {cls.count}")


Test.get_number_of_objects()  # The number of objects created: 0
t1 = Test()
t2 = Test()
t3 = Test()
Test.get_number_of_objects()  # The number of objects created: 3


# Difference between Instance method vs Class method
'''
1)  Inside instance method if we are using at least one instance variable then compulsory 
    we should declare that method as instance method
1)  Inside method, If we are using only static variables and if we are not using instance 
    variables then we have to declare that method as class method
    
2)  Inside instance method, we can access both instance and static variables
2)  Inside class method, we can access only static variables

3)  We can call instance method by using object reference
3)  We can call class method either by using object reference or by using class name
'''
