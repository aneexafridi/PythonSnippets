# ----------------Writing Data to the file
# write() - This method is used to store/write character or string into
# the file represented by the file object. It returns the 
# Number of character writen.
# Syntax:- 
# 		File_name.write(string)

# in w mode data will be overrided
file = open("Student_write.txt",mode='w')
file.write("Shahab Afridi\n")
Character_Numbers = file.write("Kohat")
print("Number of Character: ",Character_Numbers)
file.close()