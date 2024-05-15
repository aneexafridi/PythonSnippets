# --------------File Object Variables
# >>name - This shows the name of specified file.
# Syntax:-  file_Name.name

# >>mode - This shows mode(purpose) of the file.
# Syntax: - file_Name.mode

# >> close - This used to check whether file has closed or not.
# It shows True if file is closed else shows False.
# Syntax:- file_object.closed
file = open("Student_variable.txt",mode='r',encoding='utf-8')
print("File Name and with extension: ",file.name)
print("File Mode: ",file.mode)
print("File Closed or Not: ",file.closed)