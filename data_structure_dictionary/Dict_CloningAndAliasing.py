"""
Aliasing of Dict Objects: =
------------------------
=>  The process of giving another reference variable to the existing dict is called aliasing.
=>  The problem in this approach is by using one reference variable if we are changing
    content, then those changes will be reflected to the other reference variable.

Cloning of Dict Objects: copy()
------------------------
=>  To overcome aliasing problem we should go for cloning.
=>  The process of creating exactly duplicate independent object is called cloning.
=>  We can implement cloning by using copy() function.
"""

# Aliasing
dict1 = {111: "IronMan", 222: "BatMan"}
dict2 = dict1
print(dict1)  # {111: 'IronMan', 222: 'BatMan'}
print(dict2)  # {111: 'IronMan', 222: 'BatMan'}
dict1[555] = "SuperMan"
print(dict1)  # {111: 'IronMan', 222: 'BatMan', 555: 'SuperMan'}
print(dict2)  # {111: 'IronMan', 222: 'BatMan', 555: 'SuperMan'}

# Cloning
# By using copy() method
dict1 = {111: "IronMan", 222: "BatMan"}
dict2 = dict1.copy()
print(dict1)  # {111: 'IronMan', 222: 'BatMan'}
print(dict2)  # {111: 'IronMan', 222: 'BatMan'}
dict1[555] = "SuperMan"
print(dict1)  # {111: 'IronMan', 222: 'BatMan', 555: 'SuperMan'}
print(dict2)  # {111: 'IronMan', 222: 'BatMan'}

"""
Difference between = Operator and copy() Function
    = Operator meant for aliasing
    copy() Function meant for cloning
"""
