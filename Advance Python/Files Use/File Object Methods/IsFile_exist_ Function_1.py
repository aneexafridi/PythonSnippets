# --------check File exists or Not
# isfile() - This method is used to check whether specified file is exists or not.
# This method belongs to path module which is which is sub module of os module.
# Syntax:-
# import os
# os.path.isfile(file_Name)

import os
print("If exist it will return True else False")
print(os.path.isfile("Student_Method.txt"))

if os.path.isfile("Student_Method.txt"):
	file = open("Student_Method.txt")
	print("File open")
	file.close()
else:
	print("File open does not exist")