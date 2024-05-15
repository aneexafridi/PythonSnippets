# ---------------Deletion
# we can delete an item of dictionary or entire dictionary
# using del statement.

# Deleting an item:
# 		del Dict[key]
# Deleting entire Dictionary:
# 		del Dict

Dict = {1:"one",2:"two",3:"three"}
print(Dict)
del Dict[2]
print("After deleted the Dict[2]")
print(Dict)
del Dict # After we cann't access anymore
# the Dict in this program
print("After deleted the entire Dict")
print(Dict) # output this NameError: name 'Dict' is not defined