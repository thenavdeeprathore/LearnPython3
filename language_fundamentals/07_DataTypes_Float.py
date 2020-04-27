"""
Float Data Type:
----------------
=> We can use float data type to represent floating point values (decimal values)
    Eg: f = 1.234
    type(f) float
=> We can also represent floating point values by using exponential form (Scientific Notation)
    Eg: f = 1.2e3  instead of 'e' we can use 'E'
    print(f) 1200.0

=> The main advantage of exponential form is we can represent big values in less memory.

***Note:
We can represent int values in decimal, binary, octal and hexa decimal forms. But we
can represent float values only by using decimal form.
"""
f = 12.456
print(f)  # 12.456
print(type(f))  # <class 'float'>


e = 1.2e3  # 1.2 * 10*10*10
print(e)  # 1200.0
print(type(e))  # <class 'float'>

e = 1.2E3  # 1.2 * 10*10*10
print(e)  # 1200.0
print(type(e))  # <class 'float'>
