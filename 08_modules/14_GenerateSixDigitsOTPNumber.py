# Program to generate random OTP and passwords

from random import *

print(randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9))
# space will come
# 2 4 6 1 8 6

print(randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9), sep='')
# No space will come after using sep=''
# 983514


otp = ''
for i in range(6):
    otp = otp + str(randint(0, 9))

print("Otp: ", otp)

# generate 6 length password where odd index are alphabets and even index are digits
alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
digits = "0123456789"

print(choice(alphabets), choice(digits), choice(alphabets), choice(digits), choice(alphabets), choice(digits), sep='')

print(choice(alphabets + digits), choice(alphabets + digits), choice(alphabets + digits),
      choice(alphabets + digits), choice(alphabets + digits), choice(alphabets + digits), sep='')
