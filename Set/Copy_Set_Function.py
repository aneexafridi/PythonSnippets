# -----Copying Elements
# copy() method is used to copy existing set's elements into another set.
# Syntax:- 
# 	new_Set_Name= set_Name.copy()
Set_1 = {1,2,3,"Equal"}
Set_2 = Set_1.copy()
print(Set_1)
print(id(Set_1))
print(Set_2)
print(id(Set_2))

# Note  Set_2 = Set_1  both id same
# but in copy case Set_2 = Set_1 does not same