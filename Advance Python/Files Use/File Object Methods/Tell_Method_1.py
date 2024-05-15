# -----------------Tell Method
# tell() -This method is used to find current position of file pointer from
# beginning of the file.Position starts from 0.
# Syntax: file_object.tell()

file = open("Student_Method.txt",mode='r')
# return the pointer or position
print("cursor: ",file.tell()) 
print("Read character: ",file.read(7))
print("cursor: ",file.tell())
file.close()