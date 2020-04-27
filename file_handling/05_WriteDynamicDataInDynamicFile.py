fname = input("Enter file name: ")

f = open(fname, "w")

while True:
    data = input("Enter some data: ")
    f.write(data + "\n")
    option = input("Do you want to enter some more data [Yes|No]:")
    if option.lower() == "no":
        break
print("Your provided data written to the file successfully")
f.close()
