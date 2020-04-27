# module1.py
def add(a, b):
    print("module 1")
    print(a + b)


# module2.py
def add(a, b):
    print("module 2")
    print(a + b)


# test.py
from module1 import *
from module2 import *

add(10, 20)

# This will print most recent module add which is module2


# How to print both add methods:
# Way 1:
import module1
import module2

module1.add(1, 2)
module2.add(2, 3)


# Way 2:
from module1 import add as a1
from module2 import add as a2

a1.add(10, 20)
a2.add(20, 30)
