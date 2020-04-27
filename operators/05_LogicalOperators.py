"""
4) Logical Operators: and, or, not
----------------------------------
We can apply for all types.

 For boolean Types Behaviour:
        and  If both arguments are True then only result is True
        or  If at-least one argument is True then result is True
        not  Complement

        True and False  False
        True or False  True
        not False  True

 For non-boolean Types Behaviour:
        0 means False
        non-zero means True
        empty string is always treated as False
"""

# and
print(True and True)  # True
print(True and False)  # False
print(False and True)  # False
print(False and False)  # False
# If first argument is zero then result is zero otherwise result is y
print(10 and 20)  # 20
print(0 and 20)  # 0


# or
print(True or True)  # True
print(True or False)  # True
print(False or True)  # True
print(False or False)  # False
# If x evaluates to True then result is x otherwise result is y
print(10 or 20)  # 10
print(0 or 20)  # 20


# not
print(not True)  # False
print(not False)  # True
# If x is evaluates to False then result is True otherwise False
print(not 10)  # False
print(not 0)  # True
print(not "")  # True
