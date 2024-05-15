# -------------keys() Method
# This method return a sequence of keys from the dictionary.
# Syntax:-- Dict_Name.keys()

Dict = {1:"one",2:"two",3:"three"}
print(Dict)

print("Geting the keys of Dict")
print(Dict.keys())
print("Dict.keys return List in Tuple")
# We can convert Tuple into List
# simple List =list(Tuple)
# Dict.keys return Tuple that's why 
#i used for loop to display

for u in Dict.keys():
	print(u,end=' ')
