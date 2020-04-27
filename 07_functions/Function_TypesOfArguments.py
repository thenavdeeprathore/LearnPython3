# ###################### Types of arguments in 07_functions ######################
"""
Types of Arguments
def f1(a,b):
    ------
    ------
    ------
f1(10,20)

a, b are formal arguments where as 10, 20 are actual arguments

There are 4 types of actual arguments are allowed in Python.
1) Positional / Required
2) Default
3) Keyword
4) Variable length
"""


# ###################### 1) positional / required arguments to the 07_functions
'''
=> These are the arguments passed to function in correct positional order.
    def sub(a, b):
        print(a-b)
        sub(100, 200)
        sub(200, 100)
=> The number of arguments and position of arguments must be matched.
    - If we change the order then result may be changed.
    - If we change the number of arguments then we will get error.

# NOTE : positional argument must come first before keyword argument
'''


# case 1:
def user_info(name, age, city):
    print(f"Hi, my name is {name} and my age is {age} and I live in {city}")


user_info("Vicky", 30, "Tokyo")  # Hi, my name is Vicky and my age is 30 and I live in Tokyo
user_info(30, "Tokyo", "Chris")  # Hi, my name is 30 and my age is Tokyo and I live in Chris
# user_info("John", 30)  # TypeError: user_info() missing 1 required positional argument: 'city'


# case 2:
def sub(a, b):
    print(a - b)


sub(200, 100)  # 100
sub(100, 200)  # -100
# sub(10)  # TypeError: sub() missing 1 required positional argument: 'b'


# ###################### 2) Keyword arguments to the 07_functions
'''
We can pass argument values by keyword i.e by parameter name.
Here the order of arguments is not important but number of arguments must be matched.


NOTE: positional argument must come first before keyword argument
We can use both positional and keyword arguments simultaneously but first we
have to take positional arguments and then keyword arguments,
otherwise we will get an error.

NOTE: once the keyword arg starts, next all args must be keyword args
'''


# case 1:
def user_info(name, age, city):
    print(f"Hi, my name is {name} and my age is {age} and I live in {city}")


user_info(name="Vicky", age=30, city="Tokyo")  # Hi, my name is Vicky and my age is 30 and I live in Tokyo
user_info(age=23, city="London", name="Chris")  # Hi, my name is Chris and my age is 23 and I live in London


# case 2:
def sub(a, b):
    print(a - b)


sub(a=200, b=100)  # 100
sub(b=100, a=200)  # 100
# sub(a=100)  # TypeError: sub() missing 1 required positional argument: 'b'


# case 3:
# NOTE: once the keyword argument starts, next all args must be keyword args
# NOTE: positional argument must come first before keyword argument
def emp_data(emp_id, emp_name, emp_sal):
    print(emp_id, emp_name, emp_sal)


emp_data(emp_id=11, emp_name="tom", emp_sal=100000)  # 11 tom 100000
emp_data(emp_name="jerry", emp_sal=200000, emp_id=12)  # 12 jerry 200000
emp_data(13, emp_name="micky", emp_sal=300000)  # 13 micky 300000
# emp_data(emp_id=14, "minnie", emp_sal=400000)  # SyntaxError: positional argument follows keyword argument


# ###################### 3) Default arguments to the 07_functions
'''
Sometimes we can provide default values for our positional arguments.
If we are not passing any name then only default value will be considered.

***Note:
After default arguments we should not take non default arguments.
SyntaxError: non-default argument follows default argument

1) def wish(name="Guest", msg="Good Morning"):  Valid
2) def wish(name, msg="Good Morning"):  Valid
3) def wish(name="Guest", msg):  Invalid 
'''


# case 1:
def greeting(name="Guest"):
    print("Hello,", name, "Good Morning")


greeting("Noddy")  # Hello, Noddy Good Morning
# In this case default value will be considered
greeting()  # Hello, Guest Good Morning


# case 2:
def user_data(user_id=111, user_name="navdeep"):
    print("User Id: ",  user_id, "User name: ", user_name)


user_data()  # User Id:  111 User name:  navdeep
user_data(222, "John")  # User Id:  222 User name:  John
user_data(333)  # User Id:  333 User name:  navdeep


# case 3:
def wish(name="Guest", msg="Good Morning"): pass  # Valid
def wish(name, msg="Good Morning"): pass  # Valid
# def wish(name="Guest", msg): pass  # SyntaxError: non-default argument follows default argument


# ###################### 4) Variable length arguments to the 07_functions
'''
=>  Sometimes we can pass variable number of arguments to our function, such type of
    arguments are called variable length arguments.
=>  We can declare a variable length argument with * symbol as follows
=>  def f1(*n):
=>  We can call this function by passing any number of arguments including zero number.
=>  Internally all these values represented in the form of tuple.

=>  After variable length argument if we are taking any normal argument then we have to provide values
    by using keywords for that normal argument
=>  More than one variable length arguments are not allowed
'''


# case 1:
def display(*n):
    print("variable length arg")


display()  # variable length arg
display(10)  # variable length arg
display(10, 20)  # variable length arg
display(10, "Nav", 20.23, 30, 40, True)  # variable length arg


# case 2: n is tuple
def display(*n):
    print(type(n))
    print(n)


display()
# <class 'tuple'>
# ()
display(10)
# <class 'tuple'>
# (10,)
display(10, 20)
# <class 'tuple'>
# (10, 20)
display(10, "Nav", 20.23, 30, 40, True)
# <class 'tuple'>
# (10, 'Nav', 20.23, 30, 40, True)


# case 3: sum of numbers
def add(*n):
    result = 0
    for x in n:
        result = result + x
    print(f'Sum is: {result}')


add()  # Sum is: 0
add(10)  # Sum is: 10
add(10, 20)  # Sum is: 30
add(10, 20, 30)  # Sum is: 60


# case 4: Multiple Variable length is not allowed
# def show(*x, *y): pass


# ###################### Positional and Variable length arguments simultaneously
# NOTE: Variable length arguments must always be the last argument

# case 1: NOTE - positional must always be the first argument
def add(x, *y):
    print(x, y)


add("Chris")  # Chris ()
add("Vicky", 10)  # Vicky (10,)
add("Rocky", 10, 20)  # Rocky (10, 20)
add("John", 10, 20, 30)  # John (10, 20, 30)


# case 2: Invalid, since positional is not the first argument
def add(*x, y):
    print(x, y)


# add("Chris")  # TypeError: add() missing 1 required keyword-only argument: 'y'
# add(10, "Vicky")  # TypeError: add() missing 1 required keyword-only argument: 'y'
# add(10, 20, "Rocky")  # TypeError: add() missing 1 required keyword-only argument: 'y'
# add(10, 20, 30, "John")  # TypeError: add() missing 1 required keyword-only argument: 'y'
add(10, 20, 30, y="gabi")  # (10, 20, 30) gabi


# ###################### Positional, Keyword and Variable length arguments simultaneously
# case 1: Valid
def add(*n, name):
    result = 0
    for x in n:
        result = result + x
    print(f'Sum by {name} is: {result}')


add(name="Chris")  # Sum by Chris is: 0
add(10, name="Vicky")  # Sum by Vicky is: 10
add(10, 20, name="Rocky")  # Sum by Rocky is: 30
add(10, 20, 30, name="John")  # Sum by John is: 60


# ###################### **kwargs {Keyword variable length arguments}
'''
We can call this function by passing any number of keyword arguments.
Internally these keyword arguments will be stored inside a dictionary.
'''


# case 1:
def display(**kwargs):
    print(kwargs)
    for k, v in kwargs.items():
        print(k, "....", v)


display()  # {}
display(name="Vicky", marks=100, age=30)
# {'name': 'Vicky', 'marks': 100, 'age': 30}
# name .... Vicky
# marks .... 100
# age .... 30
display(name="Rocky", gf1="abc", gf2="cde", gf3="efg")
# {'name': 'Rocky', 'gf1': 'abc', 'gf2': 'cde', 'gf3': 'efg'}
# name .... Rocky
# gf1 .... abc
# gf2 .... cde
# gf3 .... efg


# case 2: *args vs **kwargs
# NOTE: **kwargs must be the last
def f1(*args, **kwargs):
    print(args)  # tuple
    print(kwargs)  # dictionary


f1()
# ()
# {}
f1(10, 20, A=30, B=40)
# (10, 20)
# {'A': 30, 'B': 40}


# final case
# Variable length arg and then default value
def f1(*x, y=10):
    print(x)
    print(y)


# positional arg and then keyword arg
f1(10, 20, y=30)


# Function arguments summary:
def m1(arg1, arg2, arg3=4, arg4=8):
    print(arg1, arg2, arg3, arg4)


m1(1, 2)  # 1 2 4 8
m1(10, 20, 30, 40)  # 10 20 30 40
m1(25, 50, arg4=100)  # 25 50 4 100
m1(arg4=2, arg1=3, arg2=4)  # 3 4 4 2
# m1()  # TypeError: m1() missing 2 required positional arguments: 'arg1' and 'arg2'
# m1(arg3=10, arg4=40, 20, 30)  # SyntaxError: positional argument follows keyword argument
# m1(4, 5, arg2=6)  # TypeError: m1() got multiple values for argument 'arg2'
# m1(4, 5, arg3=5, arg5=6)  # TypeError: m1() got an unexpected keyword argument 'arg5'
