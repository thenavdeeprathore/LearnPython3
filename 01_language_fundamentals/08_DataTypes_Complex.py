"""
Complex Data Type:
-----------------
=> A complex number is of the form
        a + bj
a --> real part
b --> imaginary part
j2 = -1

=> ‘a’ and ‘b’ contain Integers OR Floating Point Values.
    3 + 5j
    10 + 5.5j
    0.5 + 0.1j

=> In the real part if we use int value then we can specify that either by decimal, octal,
binary or hexadecimal form.

=> But imaginary part should be specified only by using decimal form
"""
c = 10 + 20j
print(c)  # (10+20j)
print(type(c))  # <class 'complex'>

c = 10 + 20J
print(c)  # (10+20j)
print(type(c))  # <class 'complex'>
print(c.real)  # 10.0
print(c.imag)  # 20.0

# c = 10 + 20i  # SyntaxError: invalid syntax
