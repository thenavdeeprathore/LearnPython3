"""
Important Functions of List:
---------------------------

I. To get Information about List:
    1) len          : Returns the number of elements present in the list
    2) count        : Returns the number of occurrences of specified item in the list
    3) index        : Returns the index of first occurrence of the specified item.

II. Manipulating Elements of List:
    4) append       : To add item at the end of the list
    5) insert       : To insert item at specified index position
    6) extend       : To add all items of one list to another list
    7) remove       : To remove specified item from the list
    8) pop          : It removes and returns the last element of the list
    9) pop(index)   : It removes and returns element present at specified index from the list
    10) clear       : It removes all elements from the list

III. Ordering Elements of List:
    11) reverse     : To reverse order of elements of list.
    12) reversed    : To reverse order of elements of any data types.
    13) sort        : To sort order of elements of list.
    14) sorted      : To sort order of elements of any data types.
"""

# I. To get Information about List:

# len()
x = [10, 20, 30, 40, 50, 10, 20, 10]
print(len(x))  # 8

# count()
print(x.count(10))  # 3
print(x.count(90))  # 0

# index()
# Note: If the specified element not present in the list then we will get ValueError.
# print(x.index(100))  # ValueError: 100 is not in list
print(x.index(10))  # 0
print(x.index(50))  # 4

# Another way of doing index search is:
# list_name.index(element, start, end)
# start (Optional) - The position from where the search begins. {index}
# end (Optional) - The position from where the search ends. {len(list_name)}
print(x.index(10, 2, 6))  # 5


# II. Manipulating Elements of List:

# append()
a = []
a.append(10)
a.append(20)
a.append(30)
print(a)

# Eg: To add all elements to list up to 100 which are divisible by 10
l = []
for item in range(1, 101):
    if item % 10 == 0:
        l.append(item)
print(l)  # [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# insert()
n = [10, 20, 30, 40]
n.insert(1, 77)
print(n)  # [10, 77, 20, 30, 40]

# Note: If the specified index is greater than max index then
# element will be inserted at last position.
n.insert(100, 50)
print(n)  # [10, 77, 20, 30, 40, 50]

# Note: If the specified index is smaller than min index then
# element will be inserted at first position.
n.insert(-100, 70)
print(n)  # [70, 10, 77, 20, 30, 40, 50]

"""
append()
In List when we append any element it will come in last i.e. it will be the last element

insert()
In List we can insert any element in particular index number
"""

# extend()
order1 = ["Chicken", "Mutton", "Fish"]
order2 = ["burger", "pizza"]
order1.extend(order2)
print(order1)  # ['Chicken', 'Mutton', 'Fish', 'burger', 'pizza']
print(order2)  # ['burger', 'pizza']

# Manipulating case 1: append with list object
l1 = [10, 20, 30]
l2 = [40, 50]
l1.append(l2)
print(l1)  # [10, 20, 30, [40, 50]]
print(len(l1))  # 4

# Manipulating case 2: append with a str
l1 = [10, 20, 30]
l1.append("NAV")
print(l1)  # [10, 20, 30, 'NAV']
print(len(l1))  # 4

# Manipulating case 3: extend with a ste
l1 = [10, 20, 30]
l1.extend("NAV")
print(l1)  # [10, 20, 30, 'N', 'A', 'V']
print(len(l1))  # 6

# remove()
l = [10, 20, 30, 10, 20, 30, 40, 50]
l.remove(50)
print(l)  # [10, 20, 30, 10, 20, 30, 40]

# If the item present multiple times then only first occurrence will be removed.
l.remove(10)
print(l)  # [20, 30, 10, 20, 30, 40, 50]

# If the specified item not present in list then we will get ValueError
# l.remove(90)  # ValueError: list.remove(x): x not in list

# Note: Before using remove() method first we have to check specified element
# present in the list or not by using in operator.
l = [1, 2, 3, 4, 5]
print("Before removal: ", l)
x = 7
if x in l:
    l.remove(x)
    print("After removal: ", l)
else:
    print(x, "not present in the list")

# How to remove all occurrences?
l = [1, 1, 1, 1, 2, 2, 2, 3, 3, 3]
x = 2
print("Before removal: ", l)
while True:
    if x in l:
        l.remove(x)
    else:
        break
print("After removal: ", l)

# pop()
l = [10, 20, 30]
print(l.pop())  # 30
print(l)  # [10, 20]

# If the list is empty then pop() function raises IndexError
l = []
# print(l.pop())  # IndexError: pop from empty list

"""
Note:
1) pop() is the only function which manipulates the list and returns some value
2) In general we can use append() and pop() functions to implement stack data structure
   by using list, which follows LIFO(Last In First Out) order.
   
In general we can use pop() function to remove last element of the list. But we can use to
remove elements based on index.

n.pop(index)  To remove and return element present at specified index.
n.pop()  To remove and return last element of the list
"""

n = [10, 20, 30, 40, 50, 60]
print(n.pop())  # 60
print(n.pop(3))  # 40
# print(n.pop(10))  # IndexError: pop index out of range

"""
remove() vs pop()
-----------------
remove():
1) We can use to remove specified element from the List.
2) It does not return any value. 
3) If specified element is not available then we get ValueError.

pop() pop(index):
1) We can use to remove last element from the List or specified index list
2) It returns removed element.
3) If List is empty then we get IndexError.
"""

# clear()
l = [10, 20, 30, 40]
l.clear()
print(l)  # []

"""
Note: 
List Objects are dynamic. i.e based on our requirement we can increase and decrease the size.

append(), insert(), extend()  for increasing the size / grow able nature
remove(), pop(), pop(index), clear()  for decreasing the size / shrinking nature
"""


# III. Ordering Elements of List:

# reverse()
l = [10, 20, 30, 40]
print(l)  # [10, 20, 30, 40]
l.reverse()
print(l)  # [40, 30, 20, 10]

# reversed()
x = [1, 2, 3, 4]
print(x)  # [1, 2, 3, 4]
r = reversed(x)
l = list(r)
print(l)  # [4, 3, 2, 1]


s = "python"
# s.reverse()  # AttributeError: 'str' object has no attribute 'reverse'

r = reversed(s)
for x in r:
    print(x)

"""
reverse() vs reversed()
-----------------------
reverse():
# list specific function
# No new object will be created
# only applicable for list data type

reversed():
# Python inbuilt function
# New object will be created
# reversed() supports str type and all other types
"""

# sort()
"""
# For numbers  Default Natural sorting Order is Ascending Order
# For Strings  Default Natural sorting order is Alphabetical Order
# Note: To use sort() function, compulsory list should contain only homogeneous elements.
# Otherwise we will get TypeError
"""
l = [5, 3, 1, 2, 6, 4]
print(l)  # [5, 3, 1, 2, 6, 4]
l.sort()  # Ascending
print(l)  # [1, 2, 3, 4, 5, 6]
l.sort(reverse=True)  # Reverse
print(l)  # [6, 5, 4, 3, 2, 1]

s = ['dog', 'cat', 'parrot', 'kola']
print(s)  # ['dog', 'cat', 'parrot', 'kola']
s.sort()  # Ascending
print(s)  # ['cat', 'dog', 'kola', 'parrot']
s.sort(reverse=True)  # Reverse
print(s)  # ['parrot', 'kola', 'dog', 'cat']

# sorted()
l1 = [300, 100, 500, 400]
print(l1)  # [300, 100, 500, 400]
l2 = sorted(l1)
print(l2)  # [100, 300, 400, 500]

"""
sort() vs sorted()
-----------------------
sort():
# list specific function
# No new object will be created
# only applicable for list data type

sorted():
# Python inbuilt function
# New object will be created
# supports all data types
"""
