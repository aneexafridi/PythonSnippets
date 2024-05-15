# -----------------Seek Method
# see(position) - This method is used to remove file pointer from one position
# to another position from beginning of the file.Position starts from 0 and 
# It must be positive integer.
# Syntax:-- 
# 		file_object.seek(position)
file = open("Student_Method.txt",mode='r')
print(file.readline())
# seek method start from 0 always
file.seek(16) # 0-16
file.seek(10) # 0-10
print(file.read())
file.close()