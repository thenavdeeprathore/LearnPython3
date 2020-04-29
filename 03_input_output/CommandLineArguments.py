"""
COMMAND LINE ARGUMENTS
----------------------
sys --> module
argv --> variable

=>  argv is not Array it is a List. It is available in sys Module.
=>  The Argument which are passing at the time of execution are called Command Line Arguments.

Eg: py test.py 10 20 30
Here 10 20 30 are command line arguments

Note: argv[0] represents Name of Program. But not first Command Line Argument.
argv[1] represent First Command Line Argument.

import argv
print(type(argv))

# Note 1:
# Usually space is separator between command line arguments. If our command line argument
# itself contains space then we should enclose within double quotes (but not single quotes)

# Note 2:
# Within the Python program command line arguments are available in the String form.
# Based on our requirement, we can convert into corresponding type by using type casting methods.

# Note 3:
# If we are trying to access command line arguments with out of range index then we will get Error.
"""
from sys import argv

print("The Number of Command Line Arguments:", len(argv))
print("The List of Command Line Arguments:", argv)
print("argv[0]: ", argv[0])  # argv[0]:  CommandLineArguments.py
print("argv[1]: ", argv[1])  # argv[1]:  10
print("argv[2]: ", argv[2])  # argv[2]:  20
print("argv[3]: ", argv[3])  # argv[3]:  30
print("Command Line Arguments one by one:")
for x in argv:
    print(x)
# The Number of Command Line Arguments: 4
# The List of Command Line Arguments: ['CommandLineArguments.py', '10', '20', '30']
# Command Line Arguments one by one:
# CommandLineArguments.py
# 10
# 20
# 30

'''
# space is separator
print(argv[1])

py test.py Sunny Leone
Sunny

py test.py 'Sunny Leone'
'Sunny

py test.py "Sunny Leone"
Sunny Leone 
'''

# Type casting
print("Sum: ", int(argv[1]) + int(argv[2]) + int(argv[3]))  # Sum:  60

# IndexError
print(argv[100])
