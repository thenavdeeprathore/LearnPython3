"""
5) Bitwise Operators:
--------------------
- We can apply these operators bitwise.
- These operators are applicable only for int and boolean types.
- By mistake if we are trying to apply for any other type then we will get Error.
- &, |, ^, ~, <<, >>


&    If both bits are 1 then only result is 1 otherwise result is 0
|    If at-least one bit is 1 then result is 1 otherwise result is 0
^    If bits are different then only result is 1 otherwise result is 0
~    bitwise complement operator
<<   Bitwise Left Shift
>>   Bitwise Right Shift

Note:
----
- The most significant bit acts as sign bit.
    0 value represents +ve number
    1 value represents -ve number
- Positive numbers will be represented directly in the memory where as -ve numbers will
be represented indirectly in 2's complement form.

1's compliment form:
-------------------
1    0
0    1

2's compliment form:
-------------------
2's compliment = 1's compliment + 1
"""

print(4 & 5)
# print(10.5 & 20.5)  # TypeError: unsupported operand type(s) for &: 'float' and 'float'
print(True & True)
print(True & False)
print(False & True)
print(False & False)

print(bin(4))
print(bin(5))

print(4 & 5)  # 4
print(4 | 5)  # 5
print(4 ^ 5)  # 1
