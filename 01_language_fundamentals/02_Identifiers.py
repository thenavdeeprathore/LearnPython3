# Variable name or class name or method name are known as Identifiers


# variable name
x = 10


# function name
def f1():
    pass


# class name
class Test:
    pass


# Rules to define Identifiers:
"""
1)  alphabets {both upper and lower case},
    digits {0 to 9},
    underscore {_}
"""
cash = 100
# ca$h = 100  # SyntaxError: invalid syntax


"""
2)  Identifiers should not starts with a digit
"""
total123 = 10
# 123total = 100  # SyntaxError: invalid syntax


"""
3)  Case-sensitive programming language.
"""
total = 10
TOTAL = 20
print(total)  # 10
print(TOTAL)  # 20

"""
4)  Python keywords can't be used for Identifiers
"""
x = 10
# def = 20  # SyntaxError: invalid syntax
# if = 30  # SyntaxError: invalid syntax


"""
5)  There is no length limit for Python Identifiers
"""

# one underscore means private identifier
_a = 10  # private

# two underscore means strongly private identifier
__b = 20  # strongly private

# starts with two underscores and ends with two underscores means
# it's a language specific identifier
# __main__

# x     : public
# _x    : protected {private}
# __x   : private {strongly private}
# __x__ : magic identifier {language specific identifier}
