try:
    print('try')
    print(10/0)
except ArithmeticError as e:
    print('ArithmeticError')
except ZeroDivisionError as e:
    print('ZeroDivisionError')
except:
    print("default error")
# try
# ArithmeticError
