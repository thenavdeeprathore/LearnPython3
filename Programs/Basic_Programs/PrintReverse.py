# ------------ String -----------
# 1) [::-1]
# 2) reversed()

s = "Hello"
print("Actual String: ", s)

r = s[::-1]
print("Reverse String: ", r)

s = "World"
print("Actual String: ", s)

r = reversed(s)
o = ''.join(r)
print("Reverse String: ", o)

# ------------ Number -----------
n = 1234
print("Actual Number: ", n)

rev = 0
while n > 0:
    dig = n % 10
    rev = rev * 10 + dig
    n = n // 10

print("Reverse Number: ", rev)

