"""
Dict methods and functions:
--------------------------
len                         : Returns the number of items{key-value pairs} present in the dict
get(key)                    : Get the value associated with the specified key
get(key, default_value)     :
add =                       :
update
del d[key]
clear
del d

"""
# -------------------------------- len in Dict:
d = {100: "tom", 200: "jerry", 300: "minnie", 400: "noddy"}
# len --> Returns the number of items {key-value pair} in the dictionary
print(len(d))  # 4


# -------------------------------- get in Dict:
# d.get(key) doesn't throw an error if a key is not present
d = {100: "tom", 200: "jerry", 300: "minnie", 400: "noddy"}
print(d[300])  # minnie
# print(d[999])  # KeyError: 999
print(d.get(300))  # minnie
print(d.get(999))  # None

# d.get(key, defaultValue)
print(d.get(100, "vicky"))  # tom
print(d.get(777, "vicky"))  # vicky


# -------------------------------- Add / Update data in Dict:
'''
d[key] = value
=> If the key is not available then a new entry will be added to the dictionary with the
specified key-value pair
=> If the key is already available then old value will be replaced with new value
'''
d = {100: "tom", 200: "jerry", 300: "minnie"}
# add
d[400] = "micky"
print(d)  # {100: 'tom', 200: 'jerry', 300: 'minnie', 400: 'micky'}

# update
d[100] = "noddy"
print(d)  # {100: 'noddy', 200: 'jerry', 300: 'minnie', 400: 'micky'}

d1 = {100: "A", 200: "B"}
d2 = {300: "C", 400: "D", 100: "Overwrite"}
d1.update(d2)
print(d1)  # {100: 'Overwrite', 200: 'B', 300: 'C', 400: 'D'}


# -------------------------------- Delete data in Dict:
'''
1) del d[key]
    - It deletes entry associated with the specified key.
    - If the key is not available then we will get KeyError.
2) d.clear()
    - To remove all entries from the dictionary.
3) del d
    - To delete total dictionary. Now we cannot access d.
'''
# del d[key]
# case 1
d = {100: "tom", 200: "jerry", 300: "minnie"}
del d[200]
print(d)  # {100: 'tom', 300: 'minnie'}

# case 2
# del d[500]  # KeyError: 500

# case 3
del d[100], d[300]
print(d)  # {}

# clear()
d = {100: "tom", 200: "jerry", 300: "minnie"}
d.clear()
print(d)  # {}

# del d
d = {100: "tom", 200: "jerry", 300: "minnie"}
del d
# print(d)  # NameError: name 'd' is not defined

# pop(key)
d = {100: "tom", 200: "jerry", 300: "minnie", 400: "noddy"}
print(d.pop(200))  # jerry
# print(d.pop(777))  # KeyError: 777

# pop(key, value)
print(d.pop(777, 'mike'))  # mike

# popitem()
print(d.popitem())  # (400, 'noddy')
print(d.popitem())  # (300, 'minnie')
print(d.popitem())  # (100, 'tom')
# print(d.popitem())  # KeyError: 'popitem(): dictionary is empty'


# -------------------------------- keys values items data in Dict:
# keys()
d = {100: "tom", 200: "jerry", 300: "minnie", 400: "noddy"}
k = d.keys()
print(k)  # dict_keys([100, 200, 300, 400])
for item in k:
    print(item)

# values()
v = d.values()
print(v)  # dict_values(['tom', 'jerry', 'minnie', 'noddy'])
for item in v:
    print(item)

# items() -- key value pair
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


# setdefault()
'''
d.setdefault(k,v)
- If the key is already available then this function returns the corresponding value.
- If the key is not available then the specified key-value will be added as new item to the dictionary.
'''
d = {100: "tom", 200: "jerry", 300: "minnie"}
print(d.setdefault(400, "noddy"))
print(d)
print(d.setdefault(100, "rocky"))
print(d)

# copy():
#  To create exactly duplicate dictionary (cloned copy)
#  d1 = d.copy()
d = {100: "tom", 200: "jerry", 300: "minnie"}
d1 = d.copy()
print(d)
print(d1)
d[400] = "chris"
print(d)  # {100: 'tom', 200: 'jerry', 300: 'minnie', 400: 'chris'}
print(d1)  # {100: 'tom', 200: 'jerry', 300: 'minnie'}
