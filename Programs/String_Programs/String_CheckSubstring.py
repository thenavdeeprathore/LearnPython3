# Python | Check if a Substring is Present in a Given String
# function to check if small string is there in big string


def check(string, sub_str):
    if string.find(sub_str) == -1:
        print("NO")
    else:
        print("YES")


string = "welcome to python programming"
sub_str = "python"
check(string, sub_str)
