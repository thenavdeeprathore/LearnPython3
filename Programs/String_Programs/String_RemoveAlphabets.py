s = "a1b2c3!@#$%^&*():><efgh45"
print(s)

alphanumeric = ''

for characters in s:
    # isdigit() -- digits / numbers
    if characters.isdigit():
        alphanumeric = alphanumeric + characters
print(alphanumeric)
