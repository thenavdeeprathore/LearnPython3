s = "a1b2c3!@#$%^&*():><efgh45"
print(s)

alphanumeric = ''

for characters in s:
    # isalnum() -- alpha numeric
    if characters.isalnum():
        alphanumeric = alphanumeric + characters
print(alphanumeric)
