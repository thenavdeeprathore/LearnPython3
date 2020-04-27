try:
    print('try')
except:
    print('except')
    try:
        print('inner try')
    except:
        print('inner except')
    finally:
        print('inner finally')


# This is valid
# output:
# try




