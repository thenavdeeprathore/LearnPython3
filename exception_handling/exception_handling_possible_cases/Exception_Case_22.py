try:
    print('try')
except:
    print('except')
finally:
    print('finally')
    try:
        print('inner try')
    except:
        print('inner except')
    finally:
        print('inner finally')


# This is valid
# output:
# try
# finally
# inner try
# inner finally





