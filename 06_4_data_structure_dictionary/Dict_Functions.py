"""
Dict 07_functions:
--------------
1) len
2) get(key) or get(key, default_value)
3) add
4) update
5) setdefault(k,v)
6) del d[key]
7) clear
8) del d
9) pop(key) or pop(key, value)
10) popitem()
11) keys()
12) values()
13) items()
14) copy()
"""

# ############################## len() function ##############################
# Returns the number of items {key-value pairs} present in the dict
d = {100: "tom", 200: "jerry", 300: "minnie", 400: "noddy"}
print(len(d))  # 4

# ##############################  get(key) function ##############################
# Get the value associated with the specified key
# If the key is not present then it will return None. It wont raise any error.

# Normal approach using key
d = {100: "tom", 200: "jerry", 300: "minnie", 400: "noddy"}
print(d[300])  # minnie
# print(d[999])  # KeyError: 999

# Best approach using get(key) without raising any error
print(d.get(300))  # minnie
print(d.get(999))  # None

# ##############################  get(key, default_value) function ##############################
# Get the value associated with the specified key
# If the key is not present then it returns the default value
print(d.get(100, "vicky"))  # tom
print(d.get(777, "vicky"))  # vicky

# ##############################  add function ##############################
# d[key] = value
# If the key is not available then a new entry will be added to the dictionary with the specified key-value pair
d = {100: "tom", 200: "jerry", 300: "minnie"}
d[400] = "micky"
print(d)  # {100: 'tom', 200: 'jerry', 300: 'minnie', 400: 'micky'}

# ##############################  update() function ##############################
# d[key] = value
# If the key is already available then old value will be replaced with new value
d[100] = "noddy"
print(d)  # {100: 'noddy', 200: 'jerry', 300: 'minnie', 400: 'micky'}

d1 = {100: "A", 200: "B"}
d2 = {300: "C", 400: "D", 100: "Overwrite"}
d1.update(d2)
print(d1)  # {100: 'Overwrite', 200: 'B', 300: 'C', 400: 'D'}

# ##############################  setdefault(k,v) function ##############################
# d.setdefault(k,v)
# If the key is already available then this function returns the corresponding value.
# If the key is not available then the specified key-value will be added as new item to the dictionary.
d = {100: "tom", 200: "jerry", 300: "minnie"}
print(d.setdefault(400, "noddy"))  # noddy
print(d)  # {100: 'tom', 200: 'jerry', 300: 'minnie', 400: 'noddy'}
print(d.setdefault(100, "rocky"))  # tom
print(d)  # {100: 'tom', 200: 'jerry', 300: 'minnie', 400: 'noddy'}

# ##############################  delete key function ##############################
# del d[key]
# It deletes entry associated with the specified key.
# If the key is not available then we will get KeyError.

# case 1
d = {100: "tom", 200: "jerry", 300: "minnie"}
del d[200]
print(d)  # {100: 'tom', 300: 'minnie'}

# case 2
# del d[500]  # KeyError: 500

# case 3
del d[100], d[300]
print(d)  # {}

# ##############################  clear() function ##############################
# d.clear()
# To remove all entries from the dictionary.
d = {100: "tom", 200: "jerry", 300: "minnie"}
d.clear()
print(d)  # {}

# ##############################  delete dictionary function ##############################
# del d
# To delete total dictionary. Now we cannot access d.
d = {100: "tom", 200: "jerry", 300: "minnie"}
del d
# print(d)  # NameError: name 'd' is not defined

# ##############################  pop(key) function ##############################
# It removes the entry associated with the specified key and returns the corresponding value.
# If the specified key is not available then we will get KeyError.
d = {100: "tom", 200: "jerry", 300: "minnie", 400: "noddy"}
print(d.pop(200))  # jerry
# print(d.pop(777))  # KeyError: 777

# ##############################  pop(key, value) function ##############################
# It removes the entry associated with the specified key and returns the corresponding value.
# If the specified key is not available then it returns the default value.
print(d.pop(777, 'mike'))  # mike

# ##############################  popitem() function ##############################
# It removes an arbitrary item (key-value pair) from the dictionary and returns it
# If the dictionary is empty then we will get KeyError
print(d.popitem())  # (400, 'noddy')
print(d.popitem())  # (300, 'minnie')
print(d.popitem())  # (100, 'tom')
# print(d.popitem())  # KeyError: 'popitem(): dictionary is empty'

# ##############################  keys() function ##############################
# It returns all keys associated with dictionary.
d = {100: "tom", 200: "jerry", 300: "minnie", 400: "noddy"}
k = d.keys()
print(k)  # dict_keys([100, 200, 300, 400])
# Print all the keys
for item in k:
    print(item)

# ##############################  values() function ##############################
# It returns all values associated with dictionary.
v = d.values()
print(v)  # dict_values(['tom', 'jerry', 'minnie', 'noddy'])
# Print all the values
for item in v:
    print(item)

# ##############################  items() function ##############################
# It returns list of tuples representing key-value pairs [(k,v),(k,v),(k,v)]
i = d.items()
print(i)  # dict_items([(100, 'tom'), (200, 'jerry'), (300, 'minnie'), (400, 'noddy')])
for item in i:
    print(item)
# (100, 'tom')
# (200, 'jerry')
# (300, 'minnie')
# (400, 'noddy')

# Most commonly used approach is Dict:
for k, v in i:
    print(k, "....", v)
# 100 .... tom
# 200 .... jerry
# 300 .... minnie
# 400 .... noddy

# ##############################  copy() function ##############################
#  d1 = d.copy()
#  To create exactly duplicate dictionary (cloned copy)
# Any changes in the one won't reflect in the another dict
d = {100: "tom", 200: "jerry", 300: "minnie"}
d1 = d.copy()
print(d)  # {100: 'tom', 200: 'jerry', 300: 'minnie'}
print(d1)  # {100: 'tom', 200: 'jerry', 300: 'minnie'}
d[400] = "chris"
print(d)  # {100: 'tom', 200: 'jerry', 300: 'minnie', 400: 'chris'}
print(d1)  # {100: 'tom', 200: 'jerry', 300: 'minnie'}

# ##############################  sorted() function ##############################
d = {1: "aa", 4: "bb", 2: "cc", 3: "dd"}
print(d.keys())  # dict_keys([1, 4, 2, 3])
print(sorted(d.keys()))  # [1, 2, 3, 4]
print(sorted(d.values()))  # ['aa', 'bb', 'cc', 'dd']
print(sorted(d.items()))  # [(1, 'aa'), (2, 'cc'), (3, 'dd'), (4, 'bb')]
print(sorted(d.keys(), reverse=True))  # [4, 3, 2, 1]
print(sorted(d.values(), reverse=True))  # ['dd', 'cc', 'bb', 'aa']
print(sorted(d.items(), reverse=True))  # [(4, 'bb'), (3, 'dd'), (2, 'cc'), (1, 'aa')]
