# case 1:
try:
    print('try')
except BaseException as e:
    print('BaseException except')


# case 2:
try:
    print('try')
except Exception as e:
    print('Exception except')


