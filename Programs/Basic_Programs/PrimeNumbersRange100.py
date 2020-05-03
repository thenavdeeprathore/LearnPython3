start = 0
end = 50

for val in range(start, end + 1):

    if val > 1:
        for n in range(2, val):
            if (val % n) == 0:
                break
        else:
            print(val)
    else:
        print(val, "is not a prime number")
