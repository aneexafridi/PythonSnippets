# -----------items() Method
# this method returns an object that contains key-value
# pair of dictionary.
# The pair are stored as tuple in the object.
# Syntax: 
# 		Dict_Name.items()
Dict = {1:"one",2:"two",3:"three"}
print(Dict)
New_Dict = Dict.items()
print(New_Dict)

List = list(New_Dict)
print("Convert New_Dict into List")
print(List)
# Access by using for loop

for u in List:
	for v in u:
		print(v ,end=' ')
	print()
## another way we can display 
print("\n")
for key ,value in Dict.items():
	print(key,value)