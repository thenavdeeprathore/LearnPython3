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
