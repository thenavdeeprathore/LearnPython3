"""
Function Aliasing:
-----------------
For the existing function we can give another name, which is nothing but function aliasing.
"""


def wish(name):
    print("Hello", name)


greeting = wish
print(id(wish))  # 23041264
print(id(greeting))  # 23041264
wish("tom")  # Hello tom
greeting("jerry")  # Hello jerry

del wish
# wish("micky")  # NameError: name 'wish' is not defined
greeting("minnie")  # Hello minnie


# Note:
# =>  In the above example only one function is available but we can call that function by
#     using either wish name or greeting name.
# =>  If we delete one name still we can access that function by using alias name.
