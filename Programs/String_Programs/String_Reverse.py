# Program To REVERSE content of the given String by using slice operator
my_string = "python"
print(my_string)
print(my_string[::-1])  # nohtyp

# Program To REVERSE content of the given String by using reversed function
my_string = "java"
print(my_string)
r = reversed(my_string)
output = ''.join(r)
print(output)  # avaj
# print("".join(reversed(my_string)))  # avaj


# Program To REVERSE content of the given String by using while loop
my_string = "swift"
print(my_string)
output = ''
i = len(my_string) - 1
while i >= 0:
    output = output + my_string[i]
    i = i - 1
print(output)  # tfiws

# Program To REVERSE content of the given Number by using slice operator
my_string = 12345
my_number = str(my_string)
print(my_number)
print(my_number[::-1])  # 54321

# Program To REVERSE content of the given Number by using reversed function
my_string = 123456789
my_number = str(my_string)
print(my_number)
r = reversed(my_number)
output = ''.join(r)
print(output)  # 987654321

# Program To REVERSE content of the given Number by using while loop
my_string = 1234567
my_number = str(my_string)
print(my_number)

output = ''
i = len(my_number) - 1
while i >= 0:
    output = output + my_number[i]
    i = i - 1
print(output)  # 7654321
