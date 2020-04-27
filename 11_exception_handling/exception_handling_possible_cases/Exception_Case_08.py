# case 1:
try:
    print('try')
except:
    print('except')
else:
    print('else')

# Valid
# Output:
# try
# else


# case 2:
try:
    print('try')
    print(10 / 0)
except:
    print('except')
else:
    print('else')

# Valid
# Output:
# try
# except
