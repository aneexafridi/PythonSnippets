# -----------setdefault() Method
# this method returns the value of the specified key.
# If key is not found then it inserts key with the specified value.
# 			Note------
#    if key is found then just return that key  value
# Syntax:---
# 		Dict_Name.setdefault(key,value)

Dict = {1:"one",2:"two",3:"three"}
print(Dict)
# default set the value is None if key is not found in Dict
print(Dict.setdefault(1)) #
print("\nAfter sefdefault Dict")
print(Dict.setdefault(8,"Eghit"))
print(Dict)