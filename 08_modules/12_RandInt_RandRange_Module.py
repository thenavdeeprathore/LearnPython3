# randint() Function:
"""
To generate random integer between two given numbers (inclusive)

random()  in between 0 and 1 (not inclusive)
uniform(x,y)  in between x and y ( not inclusive)
randint(x,y)  in between x and y ( inclusive)
"""

from random import *

print(randint(1, 10))  # generate random int value between 1 and 10 (inclusive)

# randrange ([start], stop, [step])
"""
Returns a random number from range
start <= x < stop

start argument is optional and default value is 0
step argument is optional and default value is 1

randrange(10)  generates a number from 0 to 9
randrange(1,11)  generates a number from 1 to 10
randrange(1,11,2)  generates a number from 1,3,5,7,9
"""

from random import *

print(randrange(10))  # generates a number from 0 to 9
print(randrange(1, 11))  # generates a number from 1 to 10
print(randrange(1, 11, 2))  # generates a number from 1,3,5,7,9


