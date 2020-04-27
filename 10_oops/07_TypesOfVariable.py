"""
There are 3 Types of variables:
------------------------------
1) Instance variables / Object level variables
2) Static variables / Class level variables
3) Local variables / Method level variables
"""


# case 1: variables which are declared using self are instance variables
class Student:
    """ This class is developed by Nav for instance variable demo purpose """

    def __init__(self, x, y):
        self.name = x
        self.roll_no = y

    def bio(self):
        print("Hi, my name is: ", self.name)
        print("My roll number is: ", self.roll_no)


s1 = Student("Tom", 101)
s2 = Student("John", 102)
s1.bio()
s2.bio()


# case 2: variables which are declared within the class but outside the methods and constructors are static variables
class Students:
    """ This class is developed by Nav for static variable demo purpose """
    college_name = 'Harvard'

    def __init__(self, x, y):
        self.name = x
        self.roll_no = y

    def bio(self):
        print("Hi, my name is: ", self.name)
        print("My roll number is: ", self.roll_no)


s1 = Students("Tom", 101)
print(s1.college_name)
s2 = Students("John", 102)
print(s2.college_name)
s3 = Students("Mark", 103)
print(s3.college_name)


# case 3: variables which are declared inside the methods and constructors are local variables
class Local:
    """ This class is developed by Nav for local variable demo purpose """
    college_name = 'Harvard'

    def __init__(self, x, y):
        count = 0  # local variable
        self.name = x
        self.roll_no = y

    def bio(self):
        x = 10  # local variable
        print("Hi, my name is: ", self.name)
        print("My roll number is: ", self.roll_no)


s1 = Local("Tom", 101)
print(s1.college_name)
