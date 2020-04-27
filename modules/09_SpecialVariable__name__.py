# The Special Variable __name__:
"""
For every Python program, a special variable __name__ will be added internally.

This variable stores information regarding whether the program is executed as an
individual program or as a module.

If the program executed as an individual program then the value of this variable is __main__

If the program executed as a module from some other program then the value of this
variable is the name of module where it is defined.

Hence by using this __name__ variable we can identify whether the program executed
directly or as a module.
"""

# Individual program
print(__name__)  # __main__

"""
module1.py:

def f1():
    if __name__=='__main__':
        print("The code executed as a program")
    else:
        print("The code executed as a module from some other program")
f1()


test.py:

import module1
module1.f1() 


Output:
py module1.py
The code executed as a program 

py test.py
The code executed as a module from some other program {because of import statement}
The code executed as a module from some other program {because of module1.f1() statement}
"""


# To avoid calling methods during import statements:
"""
module1.py

def f1():
    print("f1 execution")
def f2():
    print("f2 execution")
def f3():
    print("f3 execution")

if __name__=='__main__':
    f1()
    f2()
    f3()
    
test.py
import module1
module1.f1()


Output:
py module1.py
f1 execution
"""
