# ---------Accessing Dictionary
# We can access the value of a dictionary by referring to 
# its key Name, inside square brackets.
# Syntax:--
# 		Dict = {1:"one",2:"Two"}
# 	
Dict = {1:"one",2:"two",3:"three"}
print(Dict)
print("\nUsing For Loop")
for u in Dict:
	print(Dict[u],end=" ")
print()
for key in Dict:
	print(key,Dict[key])
print()
print([key for key in Dict])