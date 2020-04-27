# First way:
import packages.Pack1.Module1

packages.Pack1.Module1.f1()  # function f1 in module1

# Second way: Much easier
from packages.Pack1.Module1 import f1

f1()  # function f1 in module1


# subpackages
from packages.Pack1.Module1 import f1
from packages.Pack1.Pack2.Module2 import f2

f1()
f2()
