#  Program to print the Number of Lines, Words and Characters present in the given File?

import os

fname = input("Enter file name: ")

if os.path.isfile(fname):
    print("File exists: ", fname)
    lines_count = words_count = chars_count = 0
    f = open(fname, "r")
    for line in f:
        lines_count = lines_count + 1
        words_count = words_count + len(line.split())
        chars_count = chars_count + len(line)

    print("The number of Lines:", lines_count)
    print("The number of Words:", words_count)
    print("The number of Characters: ", chars_count)
else:
    print("File doesn't exists: ", fname)
