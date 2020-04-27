# choice() Function:
"""
It won’t return random number.

It will return a random object from the given list, tuple, string etc.

choice(sequential) --> index-able sequence {list, tuple, string}
"""
from random import *

fruits = ['apple', 'orange', 'watermelon', 'grapes', 'banana', 'strawberries', 'mango']
print(choice(fruits))

cars = ('bmw', 'audi', 'mercedes', 'ferrari', 'ford')
print(choice(cars))

alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
print(choice(alphabets))

digits = '0123456789'
print(choice(digits))
