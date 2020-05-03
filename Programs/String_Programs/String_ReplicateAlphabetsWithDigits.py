# Program for the requirement, input: a4b3c2 and expected output: aaaabbbcc

s = "a4b3c2"
print(s)

output = ''

for ch in s:
    if ch.isalpha():
        a = ch
    else:
        d = int(ch)
        output = output + a * d
print(output)  # aaaabbbcc
