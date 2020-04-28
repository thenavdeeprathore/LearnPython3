"""
What is the purpose of Garbage collection
-----------------------------------------
# Garbage collector is responsible to destroy useless objects
# If object don't have any reference variables is eligible for garbage collection
# Programmer is not responsible to destroy useless objects
# To make python programs more robust by default Garbage collection is enabled
"""


# How to enable and disable GC in our program:
import gc

print(gc.isenabled())  # True
gc.disable()
print(gc.isenabled())  # False
gc.enable()
print(gc.isenabled())  # True

# constructor : __init__(self)
# Not to construct objects
# To perform initialization

# destructor : __del__(self)
# To perform cleanup activities
# GC will call destructor to perform cleanup activities just before destroying an object

import time


class Test:

    def __init__(self):
        print('Object Initialization...')

    def __del__(self):
        print('Full filling last wish and perform clean up activities...')


t = Test()
t = None
time.sleep(5)
print('End of application')
