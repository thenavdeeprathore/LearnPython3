# 1: Using slicing technique


# Python program to copy or clone a list Using the Slice Operator
def cloning(li1):
    li_copy = li1[:]
    return li_copy


li1 = [4, 8, 2, 10, 15, 18]
li2 = cloning(li1)
print("Original List:", li1)
print("After Cloning:", li2)


# 2: Using the extend() method


# Python code to clone or copy a list Using the in-built function extend()
def cloning(li1):
    li_copy = []
    li_copy.extend(li1)
    return li_copy


li1 = [4, 8, 2, 10, 15, 18]
li2 = cloning(li1)
print("Original List:", li1)
print("After Cloning:", li2)


# 3: Using the list() method


# Python code to clone or copy a list Using the in-built function list()
def cloning(li1):
    li_copy = list(li1)
    return li_copy


li1 = [4, 8, 2, 10, 15, 18]
li2 = cloning(li1)
print("Original List:", li1)
print("After Cloning:", li2)


# 4: Using list comprehension

# Python code to clone or copy a list Using list comprehension
def cloning(li1):
    li_copy = [i for i in li1]
    return li_copy


li1 = [4, 8, 2, 10, 15, 18]
li2 = cloning(li1)
print("Original List:", li1)
print("After Cloning:", li2)


# 5: Using the append() method

# Python code to clone or copy a list Using append()
def cloning(li1):
    li_copy = []
    for item in li1:
        li_copy.append(item)
    return li_copy


li1 = [4, 8, 2, 10, 15, 18]
li2 = cloning(li1)
print("Original List:", li1)
print("After Cloning:", li2)


# 6: Using the copy() method

# Python code to clone or copy a list Using bilt-in method copy()
def cloning(li1):
    li_copy = li1.copy()
    return li_copy


li1 = [4, 8, 2, 10, 15, 18]
li2 = cloning(li1)
print("Original List:", li1)
print("After Cloning:", li2)
