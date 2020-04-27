"""
Similarity between List and Tuple:
----------------------------------
=>  In both the cases:
        Insertion order is preserved
        Duplicate objects are allowed
        Heterogeneous objects are allowed
        Index and slicing are supported


Differences between List and Tuple:
----------------------------------
List:
====
1) List objects are mutable
2) List is a Group of Comma separated Values within Square Brackets and Square Brackets are mandatory.
    Eg: l = [10, 20, 30, 40]
3) List requires more memory {performance is low}
4) Speed is low
5) List is un hashable type, we can not use as Keys for Dictionaries because Keys should be Hashable and Immutable.
6) Comprehension concept is applicable for list
7) If the content is not fixed, then we should go for list

Tuple:
=====
1) Tuple objects are immutable
2) Tuple is a Group of Comma separated Values within Parenthesis and Parenthesis are optional.
    Eg: t = (10, 20, 30, 40)
        t = 10, 20, 30, 40
3) Tuple requires less memory {performance is high}
4) Speed is high
5) Tuple is hashable type, we can be use as Keys for Dictionaries because Keys should be Hashable and Immutable.
6) Comprehension concept is NOT applicable for tuple
7) If the content is fixed, then we should go for tuple
"""

import collections

l = [10, 20, 30]
t = (100, 200, 300)

# List is un-hashable
print(isinstance(l, collections.Hashable))  # False
# Tuple is hashable
print(isinstance(t, collections.Hashable))  # True
