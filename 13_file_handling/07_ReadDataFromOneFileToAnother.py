# Write a program to read data from one file (input.txt) and write to another file (output.txt)

# Make sure input.txt file is already created

f1 = open("../13_file_handling/input.txt", "r")
f2 = open("../13_file_handling/output.txt", "w")

data = f1.read()
f2.write(data)

f1.close()
f2.close()
print("Data is copied from one file to another successfully")
