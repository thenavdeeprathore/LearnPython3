# Program to sort characters of the string, first alphabet symbols followed by digits

s = 'B4A1D3'
print(s)  # B4A1D3

# first digits then alphabets
sort_string = sorted(s)
print(sort_string)  # ['1', '3', '4', 'A', 'B', 'D']

# first alphabets then digits
alphabets = []
digits = []

for ch in s:
    if ch.isalpha():
        alphabets.append(ch)
    else:
        digits.append(ch)
print(alphabets)  # ['B', 'A', 'D']
print(digits)  # ['4', '1', '3']
output = ''.join(sorted(alphabets) + sorted(digits))
print(output)  # ABD134

