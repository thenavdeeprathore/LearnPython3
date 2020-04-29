"""
Output Statements:
------------------
We can use print() function to display output.

=>   print() without any argument
    Just it prints new line character

Note:
=>   If both arguments are String type then + operator acts as concatenation operator.
=>   If one argument is string type and second is any other type like int then we will get Error.
=>   If both arguments are number type then + operator acts as arithmetic addition operator.
"""
# case 1: Just it prints new line character
print()

# case 2:
print("Hello World")
# We can use escape characters also
print("Hello \n World")
print("Hello\tWorld")
# We can use repetition operator (*) in the string
print(10 * "Hello")
print("Hello" * 10)
# We can use + operator also
print("Hello" + "World")

# case 3:
print("Hello" + "World")  # HelloWorld
print("Hello", "World")  # Hello World

# case 4:
a, b, c = 10, 20, 30
print("the values are: ", a, b, c)  # The Values are : 10 20 30

# NOTE: By default output values are separated by space.
# If we want we can specify separator by using "sep" attribute
a, b, c = 10, 20, 30
print(a, b, c)  # 10 20 30
print(a, b, c, sep='')  # 102030
print(a, b, c, sep=' ')  # 10 20 30
print(a, b, c, sep=',')  # 10,20,30
print(a, b, c, sep=':')  # 10:20:30

# case 5: print() with end attribute
# Note: The default value for end attribute is \n, which is nothing but new line character.
print("hello")
print("good")
print("morning")
# If we want output in the same line with space
print("hello", end=' ')
print("good", end=' ')
print("morning")
# hello good morning

# case 6: print(object) statement
l = [10, 20, 30, 40]
t = (10, 20, 30, 40)
print(l)
print(t)

# case 7: print (formatted string)
'''
1) %i  int
2) %d  int
3) %f  float
4) %s  String type

Syntax: print("formatted string" %(variable list))
'''
a = 10
b = 20
c = 30
print("a value is %i" % a)
print("b value is %d and c value is %d" % (b, c))


# case 8: Different ways to print statements in Python3
eid = int(input("Enter your id: "))
ename = input("Enter your name: ")
esal = float(input("Enter your salary: "))

print(eid)
print(ename)
print(esal)

print(eid, ename, esal)

print("Employee ID: ", eid)
print("Employee Name: ", ename)
print('Employee Salary: ', esal)

print(f"Employee ID: {eid}")
print(f"Employee Name: {ename}")
print(f"Employee Salary: {esal}")

print("Emp id={} Emp name={} Emp sal={}".format(eid, ename, esal))
print("Emp id={0} Emp name={1} Emp sal={2}".format(eid, ename, esal))
print("EmpID=%d EmpName=%s EmpSal=%g" % (eid, ename, esal))
