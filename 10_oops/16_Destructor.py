"""
Destructors:
-----------
=>  Destructor is a special method and the name should be __del__
=>  Just before destroying an object Garbage Collector always calls destructor to perform
    clean up activities (Resource de-allocation activities like close database connection etc).
=>  Once destructor execution completed then Garbage Collector automatically destroys
    that object.

Note: The job of destructor is not to destroy object but just to perform clean up activities.
"""
import time


# case 1:
class Test:

    def __init__(self):
        print('Object Initialization...')

    def __del__(self):
        print('Full filling last wish and performing clean up activities...')


t = Test()
t = None  # object doesn't have any reference variable now
# Object Initialization...
# Full filling last wish and performing clean up activities...
time.sleep(2)
print('End of application')
# End of application


# case 2:
class Test:

    def __init__(self):
        print('Object Initialization...')

    def __del__(self):
        print('Full filling last wish and performing clean up activities...')


t1 = Test()
t2 = Test()
# Object Initialization...
# Object Initialization...
time.sleep(2)
print('End of application')
# Full filling last wish and performing clean up activities...
# Full filling last wish and performing clean up activities...

'''
Important conclusion:
--------------------
Once control reached end of program, all objects which are created are by default eligible
gor GC

Note: If the object does not contain any reference variable then only it is eligible fo GC. ie
if the reference count is zero then only object eligible for GC.
'''


# case 3:
import sys
class Test1:

    def __init__(self):
        print('constructor execution...')

    def __del__(self):
        print('destructor execution...')


d1 = Test1()
d2 = d1
d3 = d1
# Note: For every object, Python internally maintains one default reference variable self.
print(sys.getrefcount(d1))  # 4
del d1
time.sleep(2)
print("object not yet destroyed after deleting d1")
del d2
time.sleep(2)
print("object not yet destroyed after deleting d2")
print("I am trying to delete last reference variable...")
del d3
print('End of application!!!')
# constructor execution...
# object not yet destroyed after deleting d1
# object not yet destroyed after deleting d2
# I am trying to delete last reference variable...
# destructor execution...
# End of application!!!


# Q1) What is the difference between del t1 and t1 = None
# If we don't want object and corresponding reference variable then we have to use del t1
# If we want reference variable but not object then we have to use t1 = None


# Q2) How to find the number of reference count of an object
# Note: For every object, Python internally maintains one default reference variable self.
# import sys
# print(sys.getrefcount(t1))


# Q3) Difference between constructor and destructor
# constructor : __init__(self)
# To perform initialization
# PVM will execute constructor immediately after creating an object

# destructor : __del__(self)
# To perform cleanup activities
# GC will execute destructor to perform cleanup activities just before destroying an object
