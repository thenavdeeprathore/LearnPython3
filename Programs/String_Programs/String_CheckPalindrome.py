def isPalindrome(s):
    rev = ''.join(reversed(s))

    if s == rev:
        return True
    return False


s = "malayalam"
pal_check = isPalindrome(s)

if pal_check:
    print("Yes")
else:
    print("NO")
