# There are 3 Types of methods:
# Instance methods / Object related methods
# Class methods / class related methods
# Static methods / utilities methods


# case 1: methods which are declared using self are instance methods
class Student:
    """ This class is developed by Nav for instance methods demo purpose """
    college_name = 'Harvard'

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


# case 2: methods which are declared using @classmethod with cls variable
class Student:
    """ This class is developed by Nav for class methods demo purpose """
    college_name = 'Harvard'

    def __init__(self, x, y):
        self.name = x
        self.roll_no = y

    def bio(self):
        print("Hi, my name is: ", self.name)
        print("My roll number is: ", self.roll_no)

    @classmethod
    def get_college_name(cls):
        print("College name is: ", cls.college_name)  # cls is mandatory for class methods


s1 = Student("Vicky", 101)
s1.bio()
Student.get_college_name()


# case 3: methods which are declared using @staticmethod without self and cls variables
class Student:
    """ This class is developed by Nav for static methods demo purpose """
    college_name = 'Harvard'

    def __init__(self, x, y):
        self.name = x
        self.roll_no = y

    def bio(self):
        print("Hi, my name is: ", self.name)
        print("My roll number is: ", self.roll_no)

    @classmethod
    def get_college_name(cls):
        print("College name is: ", cls.college_name)  # cls is mandatory for class methods

    @staticmethod
    def results(x, y):
        print("My result is: ", (x+y)/2)


# instance
s1 = Student("Rocky", 102)
s1.bio()

# class
Student.get_college_name()

# static
s1.results(10, 20)  # @staticmethod is mandatory
Student.results(30, 40)  # @staticmethod is not mandatory, will be treated as instance method
