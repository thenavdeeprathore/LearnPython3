s = "a1b2c3!@#$%^&*():><efgh45"
print(s)

alphanumeric = ''

for characters in s:
    # isalpha() -- alphabets
    if characters.isalpha():
        alphanumeric = alphanumeric + characters
print(alphanumeric)
