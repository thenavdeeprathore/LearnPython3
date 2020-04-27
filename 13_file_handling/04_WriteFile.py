# Write file
"""
We can write character data to the text files by using the following 2 methods.
1) write(str)
2) writelines(list of lines)


In the case of f.writelines(list of lines)
    - Instead of list, we can pass tuple, set and dict also
    - In the case of dict, only keys will be added and keys should be string type only
    - But if we want to add values then we have to write the code explicitly

# Way 1
data = {100:"tom", 200:"jerry"}
f.writelines([data[100], data[200]])

# Way 2
f.writelines(data.values())

# Note: While writing data by using write() or writelines() method, compulsory we have to provide
# line separator(\n), otherwise total data should be written to a single line.
"""

# ------------------------ write ---------------------------
# case 1: write
f = open("abcd.txt", "w")
f.write("Hello")
f.write("Vicky")
f.write("How are you?")

print("Data written to the file successfully using write method")
f.close()
# HelloVickyHow are you?

# case 2: write using \n
f = open("abcd.txt", "w")
f.write("Hello" + "\n")
f.write("Vicky" + "\n")
f.write("How are you?" + "\n")

print("Data written to the file successfully using write method \\n ")
f.close()
# Hello
# Vicky
# How are you?


# ------------------------ writelines ---------------------------
f = open("abcd.txt", 'w')
list = ["sunny\n", "katrina\n", "kiara\n", "deepika\n"]
f.writelines(list)
print("List of lines written to the file successfully using writeline method")
f.close()

# Note: While writing data by using write() or writelines() method, compulsory we have to provide
# line separator(\n), otherwise total data should be written to a single line.
