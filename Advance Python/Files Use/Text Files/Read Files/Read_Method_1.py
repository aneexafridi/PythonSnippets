# ------------Reading Data from file
# read(size) - This method is used to read data/content from
# a file and returns it as string in text mode or bytes in binary mode.
# Syntax:-- file_object.read(size)

# Where size represents the number of bytes to be read from the beginning
# of the file.

# When size is omitted or negative,the entire contents of the file will be
# read and returned.

# If the end of the file has been reached,file_name.read() wil return an
# Empty string("")

file = open("Read_Data.txt",mode='r')
print(file.read())
file.close()
print("First done...")
print()

file = open("Read_Data.txt",mode='r')
print(file.read(9))
file.close()
print("Second done...")