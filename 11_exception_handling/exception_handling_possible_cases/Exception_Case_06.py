# case 1:
try:
    print('try')
finally:
    print('finally')


# This is Valid but abnormal termination on exception
# output:
# try
# finally


# case 2:
try:
    print('try')
    print(10 / 0)
finally:
    print('finally')

# try
# finally
# abnormal termination
# ZeroDivisionError: division by zero
