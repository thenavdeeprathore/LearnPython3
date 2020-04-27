"""
What is instance Variable?
-------------------------
# If the value of variable varied from object to object
# For every object a different copy will be created

Where do we declare instance Variable?
-------------------------------------
# 1) Inside constructor by using self
# 2) Inside instance method by using self
# 3) From outside of the class by using object reference

How to access instance Variable?
-------------------------------
# within the class by using self
# from outside the class by using object reference

How to delete instance Variable?
-------------------------------
# Inside class --> del self.variableName
# Outside class --> del objectReference.variableName

NOTE:
If we change the values of instance variables of one object then those changes won't be
reflected to the remaining objects, because for every object we are separate copy of
instance variables are available.
"""


# case 1: Where do we declare instance Variable?
class Student:

    # Inside constructor by using self
    def __init__(self, x, y):
        self.name = x
        self.roll_no = y

    # Inside instance method by using self
    def info(self):
        self.marks = 50


# From outside of the class by using object reference
s1 = Student("Vicky", 101)
print(s1.__dict__)  # return the dictionary of the instance variables with the values
# {'name': 'Vicky', 'roll_no': 101}

s2 = Student("Rocky", 102)
s2.info()
print(s2.__dict__)
# {'name': 'Rocky', 'roll_no': 102, 'marks': 50}

s3 = Student("Rocky", 102)
s3.info()
s3.age = 30
print(s3.__dict__)
# {'name': 'Rocky', 'roll_no': 102, 'marks': 50, 'age': 30}


# case 2: How to access instance Variable?
class Student:

    def __init__(self, x, y):
        self.name = x
        self.roll_no = y

    def bio(self):
        print("Hi, my name is: ", self.name)
        print("My roll number is: ", self.roll_no)


obj = Student("Man", 101)
obj.bio()
# access instance variable from outside the class by using object reference
print(obj.name, obj.roll_no)


# case 3: How to delete instance Variable?
class Test:

    def __init__(self):
        self.a = 10
        self.b = 20
        self.c = 30

    def delete(self):
        del self.c


t1 = Test()
t2 = Test()

t1.delete()
del t1.b
del t2.a

print(t1.__dict__)  # {'a': 10}
print(t2.__dict__)  # {'b': 20, 'c': 30}
