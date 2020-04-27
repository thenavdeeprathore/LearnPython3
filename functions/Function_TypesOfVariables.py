"""
Types of Variables wrt to functional programming
------------------------------------------------
Python supports 2 types of variables.

1) Global Variables
=>  The variables which are declared outside of function are called global variables.
=>  These variables can be accessed in all functions of that module.

2) Local Variables:
=>  The variables which are declared inside a function are called local variables.
=>  Local variables are available only for the function in which we declared it.i.e from
    outside of function we cannot access.
"""
# ########## Global variable
a = 10  # global variable


def f1():
    print(a)


def f2():
    print(a)


f1()  # 10
f2()  # 10


# ########## Local variable
def f1():
    b = 20  # local variable
    print(b)  # Valid


def f2():
    # print(b)  # NameError: name 'b' is not defined
    c = 30
    print(c)


f1()  # 20
f2()  # 30


# ########## global Keyword:
# We can use global keyword for the following 2 purposes:
# 1) To declare global variable inside function
# 2) To make global variable available to the function so that we can perform required modifications
# case 1:
a = 10


def f1():
    a = 100
    print(a)  # local variable


def f2():
    print(a)  # global variable


f1()  # 100
f2()  # 10


# case 2:
a = 10


def f1():
    global a  # global variable
    a = 111  # we are changing the value of global variable
    print(a)


def f2():
    print(a)  # global variable


f1()  # 111
f2()  # 111


# case 3:
def f1():
    x = 1000  # local variable
    print(x)


# def f2():
#     print(x)  # NameError: name 'x' is not defined


f1()  # 1000
f2()  # NameError: name 'x' is not defined


# case 4:
def f1():
    # global y = 777  # Invalid

    global y  # global variable
    y = 777
    print(y)


def f2():
    print(y)  # global variable


f1()  # 777
f2()  # 777


# case 5:
# Before global keyword var we can not use that variable before
i = 100


def f1():
    # print(i)  # SyntaxError: name 'i' is used prior to global declaration
    global i
    print(i)  # 100
    i = 1000
    print(i)  # 1000


f1()


# case 6:
# Note: If global variable and local variable having the same name then we can access
# global variable inside a function as follows:
n = 333


def f1():
    n = 666
    print(n)  # 666
    # globals() function returns a dictionary
    print(globals()['n'])  # 333
    print(globals().get('n'))  # 333


f1()
