"""
Destructors:
-----------
=>  Destructor is a special method and the name should be __del__
=>  Just before destroying an object Garbage Collector always calls destructor to perform
    clean up activities (Resource de-allocation activities like close database connection etc).
=>  Once destructor execution completed then Garbage Collector automatically destroys
    that object.

Note: The job of destructor is not to destroy object but just to perform clean up activities.

# constructor : __init__(self)
# Not to construct objects
# To perform initialization

# destructor : __del__(self)
# To perform cleanup activities
# GC will call destructor to perform cleanup activities just before destroying an object
"""
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
