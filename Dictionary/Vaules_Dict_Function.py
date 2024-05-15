# --------------values() Mehtod
# This Mehtod is returns a sequence of values from the dictionary.
# Syntax:--
# 		Dict_Name.values()
Dict = {1:"one",2:"two",3:"three"}
print(Dict)
print("\nall Values of Dict")
print(Dict.values())
# to access the data of Dict.values()
# Dict.values() return Tuple(List in Tuple)
for u in Dict.values():
	print(u,end=' ')

