"""
3) Local Variables:
-------------------
=>  Sometimes to meet temporary requirements of programmer, we can declare variables inside a method directly,
    such type of variables are called local variable or temporary variables.
=>  Local variables will be created at the time of method execution and destroyed once method completes.
=>  Local variables of a method cannot be accessed from outside of method.
"""


class Test:

    def m1(self):
        a = 10
        print(a)

    def m2(self):
        b = 20
        # print(a)  # NameError: name 'a' is not defined
        print(b)


t = Test()
t.m1()
t.m2()
# print(a)  # NameError: name 'a' is not defined
# print(t.a)  # AttributeError: 'Test' object has no attribute 'a'
# print(Test.a)  # AttributeError: type object 'Test' has no attribute 'a'
