# ------------Copy() Method
# This method is used to copy all the elements from exists
# Dictionary into a new Dictionary.
# Syntax:----
# 		New_Dictionary_Name=Old_Dictionary_Name.copy()

Old_Dict = {1:"one",2:"two",3:"three"}
New_Dict = Old_Dict.copy() 
print(Old_Dict)
print(id(Old_Dict))
# the id  of New dict will be change from old dict 
# because  copying  method  create new object
print(New_Dict)
print(id(New_Dict))
print("\nAfter change")
Old_Dict[2] = "TWO"
print(Old_Dict)
print(New_Dict)



