"""
Flow control describes the order in which statements will be executed at runtime.

Flow Control:
------------
1) Selection / Conditional statements
    a) if
    b) if-else
    c) if-elif-else
    d) if-elif
2) Iterative statements
    e) for
    f) while
3) Transfer statements
    g) break
    h) continue
    i) pass
    j) del
"""
# Selection / Conditional statements:

# Case 1: if-else
a = 10
if a > 20:
    print("true condition")
else:
    print("false condition")

# Case 2: with brackets
if (a == 10):
    print("true condition")
else:
    print("false condition")

# Case 3: use boolean
if True:
    print("true condition")
else:
    print("false condition")

# Case 4: use boolean numbers
if 0:  # 1 - True , 0 - False
    print("true condition")
else:
    print("false condition")

# Case 5:
print("if body") if True else print("else body")

# Case 6:
{print("if body"), print("con 1"), print("con 2")} if True else print("else body")

# Case 7: if-elif-else
x = 20
if a == 100:
    print("true")
elif a == 20:
    print("elif")
else:  # else is optional
    print("else")

# Case 8: only if block
if True:
    print("only if block")

# Case 9: only if elif block
if True:
    print("if block")
elif False:
    print("elif block")
