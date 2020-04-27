try:
    print('try')
    try:
        print('inner try')
    except:
        print('inner except')
    finally:
        print('inner finally')
except:
    print('except')


# This is valid
# output:
# try
# inner try
# inner finally



