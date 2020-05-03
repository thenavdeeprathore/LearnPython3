# Program to merge characters of 2 strings into a single string by taking characters alternatively
# Note: length of the both string should be same

s1 = 'JOHN'
s2 = 'mark'
print(s1)
print(s2)

i, j = 0, 0
output = ''

while i < len(s1) or j < len(s2):
    output = output + s1[i] + s2[j]
    i = i + 1
    j = j + 1
print(output)

# If length of the two strings are not same then it will give IndexError
