"""
3) Equality Operators: ==, !=
-----------------------------
We can apply these operators for any type even for incompatible types also.

Note:
    Chaining concept is applicable for equality operators. If at-least one comparison
returns False then the result is False. Otherwise the result is True.
"""

print(10 == 10)  # True
print(10 == 20)  # False
print(10 != 20)  # True
print(1 == True)  # True
print(10 == True)  # False
print(10 == 10.0)  # True
print(0 == False)  # True
print(False == False)  # True
print("sunny" == "sunny")  # True
print(10 == "sunny")  # False {we will not get TypeError, only false if it doesn't match}
print(10 == "10")  # False

print(10 == 10 == 10 == 10)  # True
print(10 == 20 == 30 == 40)  # False


# Difference between == operator and is operator
# ----------------------------------------------
# is --> reference comparison / address comparison
# == --> content comparison
l1 = [10, 20, 30]
l2 = [10, 20, 30]
print(id(l1))
print(id(l2))
print(l1 is l2)  # False
print(l1 == l2)  # True

l3 = l1
print(id(l1))
print(id(l3))
print(l1 is l3)  # True
print(l1 == l3)  # True
