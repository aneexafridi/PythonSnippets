# ------------with Statement
# the with Statement can be usedd while opening a file.
# When we open a file using with statement there  is no
# need to close the file explicity.
# Syntax:-
# 		with open("file_name",mode='r') as file
# 	
# in  with 	body only use file_object 
# and out of with body objec
with open("Student_Method.txt",mode='r') as file:
	print(file.read())
