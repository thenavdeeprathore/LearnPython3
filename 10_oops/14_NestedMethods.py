"""
Nested methods:
-----------------
- We can declare a method inside another method, such types of methods are called Nested methods

Advantage:
---------
- Code re-usability
"""


class Test:

    def m1(self):

        def calc(a, b):
            print("Sum: ", a + b)
            print("Mul: ", a * b)

        calc(10, 20)
        calc(100, 200)
        calc(1000, 2000)


t = Test()
t.m1()
# Sum:  30
# Mul:  200
# Sum:  300
# Mul:  20000
# Sum:  3000
# Mul:  2000000
