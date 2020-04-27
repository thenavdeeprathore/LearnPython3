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
print(s.name)
print(s.roll_no)
s.bio()

# s1 = Student(2, "John")   # this won't be an error but this approach is incorrect
s1 = Student("John", 2)
print(s1.name)
print(s1.roll_no)
s1.bio()

# doc string
print(Student.__doc__)
help(Student)
