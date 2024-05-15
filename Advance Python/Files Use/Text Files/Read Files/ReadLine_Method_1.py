# ----------------------Reading Data from file
# readline() - This method is used to read single line from a file.
# Syntax:- file_object.readline()

# readlines() - This method is used to read all lines from a file.
# It will return list of line.
# Syntax:--
# 		file_object.readlines()

file = open("Read_Data.txt",mode='r')
# print(file.readline())
for u in file.readlines():
	print(u,end='')

# print(file.readlines())
file.close()