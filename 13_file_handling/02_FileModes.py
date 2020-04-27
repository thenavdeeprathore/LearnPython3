"""
Opening a File:

- Before performing any operation (like read or write) on the file, first we have to open
that file. For this we should use Python's inbuilt function open()
- But at the time of open, we have to specify mode, which represents the purpose of
opening file.

f = open(filename, mode)


1) Open the file:
                open()
2) Read or Write or Append the file
                read() readLine() readLines()
                write()
                append()
3) Close the file
                close()

NOTE : the default operation mode is - read "r"
NOTE : to read the data file is mandatory
NOTE : to write the data file is NOT mandatory, we can create and write

modes:
    r : read
    w : write
    a : append
    r+ : read & write
    w+ : write & read
    a+ : append & read
    x : exclusive

The allowed modes in Python are:

1)  r  read
    - This is default mode.
    - open an existing file for read operation.
    - The file pointer is positioned at the beginning of the file.
    - If the specified file does not exist then we will get FileNotFoundError.
    - File is mandatory


2)  w  write
    - open an existing file for write operation.
    - If the file already contains some data then - It will overwrite existing data.
    - If the specified file is not already available then this mode will create that file.
    - File is Not mandatory


3)  a  append
    - open an existing file for append operation.
    - It wont overwrite existing data.
    - If the specified file is not already available then this mode will create a new file.
    - File is Not mandatory


4)  r+  read and write
    - To read and write data into the file.
    - If the specified file does not exist then we will get FileNotFoundError.
    - If the file already contains some data then it will be overridden.
    - The file pointer is placed at the beginning of the file.
    - File is mandatory

5)  w+  write and read
    - To write and read data.
    - If the file already contains some data then - It will overwrite existing data.
    - If the specified file is not already available then this mode will create a new file.
    - File is Not mandatory

6)  a+  append and read
    - To append and read data from the file.
    - It wont overwrite existing data.
    - If the specified file is not already available then this mode will create a new file.
    - File is Not mandatory


7)  x  write
    - To open a file in exclusive creation mode for write operation.
    - If the file already exists then we will get FileExistsError.
    - File should not be available.

Note:   All the above modes are applicable for text files.
        If the above modes suffixed with 'b' then these represents for binary files.

Eg: rb,wb,ab,r+b,w+b,a+b,xb


Q1: In which modes file should be already present?
Ans: r, r+

Q2: In which modes file should NOT be already present?
Ans: x

Q3: In which modes, over writing of existing data will be happened?
Ans: w, r+, w+

Q4: In which modes, over writing of existing data will NOT be happened?
Ans: a, a+

Q5: In which modes, a new file will be created?
Ans: w, a, w+, a+, x
"""
