# Your list `x`
x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(x)

# Split `x` up in chunks of 3
y = zip(*[iter(x)] * 3)

# Use `list()` to print the result of `zip()`
z = list(y)
print(z)

