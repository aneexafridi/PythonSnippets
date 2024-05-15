# --------------Writing Data to the file

# Writlines() - This method is used to store/write group of string (list,tuple,set)
# into the file represented by the file object.
# Syntax:-- file_name.wirtelines(group of string)

file = open("Student_Method.txt",mode='w')
List = ["Shahab\n","Afridi\n","Anees\n","Khan\n"]
Set = {1,2,3,4,5}
file.writelines(List)
file.writelines(str(Set))
file.close()
print("Success")