# make list 1 data as keys and list 2 data as values
l1 = [1, 2, 3]
l2 = ["AAA", "BBB", "CCC"]
x = zip(l1, l2)
d = dict(x)
print(d)  # {1: 'AAA', 2: 'BBB', 3: 'CCC'}

# make tuple 1 data as keys and tuple 2 data as values
t1 = (1, 2, 3)
t2 = ("AAA", "BBB", "CCC")
x = zip(t1, t2)
d = dict(x)
print(d)  # {1: 'AAA', 2: 'BBB', 3: 'CCC'}

# make set 1 data as keys and set 2 data as values
s1 = {1, 2, 3}
s2 = {"AAA", "BBB", "CCC"}
x = zip(s1, s2)
d = dict(x)
print(d)  # {1: 'CCC', 2: 'BBB', 3: 'AAA'}
