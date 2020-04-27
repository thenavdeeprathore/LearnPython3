"""
Important Functions of Set:
---------------------------

1) len                      : Returns the number of elements present in the set
2) add                      : Adds a specified item in the set
3) update                   : Adds multiple items to the set

4) remove                   : It removes the specified element from the set {KeyError}
5) discard                  : It removes the specified element from the set {No error}
6) pop                      : It removes and returns some random element from the set
7) clear                    : To remove all elements from the Set

8) union                    : Returns all elements present in both sets
9) intersection             : Returns common elements present in both sets
10) difference              : Returns elements present in x but not in y
11) symmetric_difference    : Returns elements present in either x OR y but not in both
"""

# len() --> python inbuilt function
s = {10, 20, 30, 40}
print(len(s))  # 4

# add() --> set specific method
s.add(50)
print(s)  # {40, 10, 50, 20, 30}

# update() --> To add multiple items to the set
# NOTE: Arguments are not individual elements but these are Iterable objects
# like List, Tuple, Set, Range, Str etc.
s = {10, 20}
l = [30, 40]
s.update(l)
print(s)  # {40, 10, 20, 30}
s.update(range(1, 6), "python")
print(s)  # {1, 2, 3, 4, 5, 'y', 'o', 40, 'p', 10, 'h', 't', 20, 'n', 30}

'''
Q) What is the difference between add() and update() functions in Set?

=>  We can use add() to add individual item to the Set, where as we can use update() function 
to add multiple items to Set.
    
=> add() function can take only one argument where as update() function can take any
number of arguments but all arguments should be iterable objects.

Q) Which of the following are valid?

A) s.add(10)                                VALID
B) s.add(10, 20, 30)                        INVALID
C) s.update(100)                            INVALID
D) s.update(range(1,10,2), range(0,10,2))   VALID
'''

# remove():
# It removes specified element from the set.
# If the specified element not present in the set then we will get KeyError.
s = {10, 20, 30, 40}
s.remove(20)
print(s)  # {40, 10, 30}
# s.remove(70)  # KeyError: 70

# discard():
# It removes the specified element from the set.
# If the specified element not present in the set then we won't get any error.
s = {100, 200, 300, 400}
s.discard(200)
print(s)  # {100, 400, 300}
s.discard(700)
print(s)  # {100, 400, 300}

# pop()
# Remove and return some random item
s = {10, 20, 30, 40}
print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())
# If the set is empty and if we still use pop() then we will get a KeyError
# print(s.pop())  # KeyError: 'pop from an empty set'

# clear()
# To remove all elements present in the set
s = {10, 20, 30, 40}
print(s)  # {40, 10, 20, 30}
s.clear()
print(s)  # set()


# Set specific methods for mathematical operations
# union() or |  ==> add all the elements in both the set without duplicates
s1 = {10, 20, 30, 40}
s2 = {30, 40, 50, 60}
s3 = s1.union(s2)
print(s3)  # {40, 10, 50, 20, 60, 30}
s3 = s1 | s2
print(s3)  # {40, 10, 50, 20, 60, 30}

# intersection() or &  ==> elements common in both the set
s1 = {10, 20, 30, 40}
s2 = {30, 40, 50, 60}
s3 = s1.intersection(s2)
print(s3)  # {40, 30}
s3 = s1 & s2
print(s3)  # {40, 30}

# difference() or - ==> elements present in s1 but not in s2
s1 = {10, 20, 30, 40}
s2 = {30, 40, 50, 60}
s3 = s1.difference(s2)
print(s3)  # {10, 20}
s3 = s1 - s2
print(s3)  # {10, 20}

# symmetric_difference() or ^ ==> elements present in s1 and s2 but not in both
s1 = {10, 20, 30, 40}
s2 = {30, 40, 50, 60}
s3 = s1.symmetric_difference(s2)
print(s3)  # {10, 50, 20, 60}
s3 = s1 ^ s2
print(s3)  # {10, 50, 20, 60}
