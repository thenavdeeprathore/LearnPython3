# Reloading a Module:
# By default module will be loaded only once even though we are importing multiple times

"""
module1.py:
print("This is from module1")


test.py
import module1
import module1
import module1
import module1
print("This is test module")


Output
This is from module1
This is test module
"""

# In the above program test module will be loaded only once even though we are importing
# multiple times.

# The problem in this approach is after loading a module if it is updated outside then
# updated version of module1 is not available to our program.

# We can solve this problem by reloading module explicitly based on our requirement
# We can reload by using reload() function of imp module.

# import imp
# imp.reload(module1)

"""
test.py:

import module1
import module1
from imp import reload
reload(module1)
reload(module1)
reload(module1)
print("This is test module")

In the above program module1 will be loaded 4 times in that 1 time by default and 3 times
explicitly. In this case output is
This is from module1
This is from module1
This is from module1
This is from module1
This is test module

The main advantage of explicit module reloading is we can ensure that updated version is
always available to our program.
"""
