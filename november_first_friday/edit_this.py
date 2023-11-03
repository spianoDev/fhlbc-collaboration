"""FILE MANIPULATION IN PYTHON"""

# Module that represents paths as special objects with useful methods and attributes.
from pathlib import Path


""" 1 """
# Check if 'test.txt' file exists.
# try:
#     file_path = Path("test.txt")
#     if not file_path.exists():
#         print(file_path.exists())
#         raise FileNotFoundError
# except FileNotFoundError:
#     print("The 'test.txt' file does not exist in the given file path.")
#     exit(1)












   
""" 2 """
# open() is a built-in Python function (no imports!)
# Allows you to open a file and return a corresponding file object.
# Multiple optional parameters, but the name of the file is mandatory.
# try:
#     file_path = Path("test.txt")
#     file = open(file_path)
#     print(file)
#     # print(file.read())
# except FileNotFoundError:
#     print("The 'test.txt' file does not exist in the given file path.")
#     exit(1)
















""" 3 """
# seek() allows you to navigate through a file.
# try:
#     file_path = Path("test.txt")
#     file = open(file_path)
#     print(file.read())
#     print(file.read())
#     # file.seek(0)
#     # print(file.read())
# except FileNotFoundError:
#     print("The 'test.txt' file does not exist in the given file path.")
#     exit(1)
















""" 4 """
# ADD A SECOND LINE OF CONTENT TO 'test.txt' FILE
# readline() reads a file line by line.
# try:
#     file_path = Path("test.txt")
#     file = open(file_path)
#     print(file.readline())
#     print(file.readline())
#     print(file.readline())
#     print(file.readline())
# except FileNotFoundError:
#     print("The 'test.txt' file does not exist in the given file path.")
#     exit(1)

















""" 5 """
# readlines() returns the entire file with each line stored as an element in a list.
# try:
#     file_path = Path("test.txt")
#     file = open(file_path)
#     print(file.readlines())
# except FileNotFoundError:
#     print("The 'test.txt' file does not exist in the given file path.")
#     exit(1)



















""" 6 """
# close() is used to explicitly close a file that was opened using the open().
# try:
#     file_path = Path("test.txt")
#     file = open(file_path)
#     print(file.readlines())
#     # file.close()
#     print(file.closed)
# except FileNotFoundError:
#     print("The 'test.txt' file does not exist in the given file path.")
#     exit(1)


















""" 7 """
# Use with statement to open files and no longer manually use close() to close file.
# try:
#     file_path = Path("test.txt")
#     with open(file_path) as file:
#         print(file.readlines())
#     print(file.closed)
# except FileNotFoundError:
#     print("The 'test.txt' file does not exist in the given file path.")
#     exit(1)


















""" 8 """
# Modes for opening files:
# r - Read a file (no writing)
# w - Write to a file (overwrites what was previously in the file)
# a - Appends to end a file (existing file content persists)

# with open("starter.txt", "w") as file:
#     file.write("This is a sentence.\n")
#     file.write("This is our second sentence!!\n")
#     file.write("This is my sentence!!!\n")

# with open("starter.txt", "a") as file:
#     file.write("This fourth sentence is the best!!!!\n")


# r+ - Read and write to a file (writing based on cursor)

# try:
#     file_path = Path("starter.txt")
#     with open(file_path, "r+") as file:
#         file.write("Five sentences rules!!!!!\n")
# except FileNotFoundError:
#     print("The 'starter.txt' file does not exist in the given file path.")
#     exit(1)