"""
eval():
------
eval Function take a String and evaluate the Result.
str --> int
str --> float
str --> float
str --> list
str --> tuple
str --> set
str --> dictionary
"""
# case 1:
x = eval(input("Enter any expression except str: "))
print(x)
print(type(x))
# Note: you can't enter str expression

# case 2:
x = eval("10 + 20 + 30")
print(x)  # 60
print(type(x))  # <class 'int'>

# case 3:
y = eval("10 + 20.5 + 30")
print(y)  # 60.5
print(type(y))  # <class 'float'>
