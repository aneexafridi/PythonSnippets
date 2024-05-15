#--------------key() method
# this method returns the value of the specified key.
# if key is not found then it will return None or default value.
# Syntax:--
# 		Dict.get(key,default_Value)

Dict = {1:"one",2:"two",3:"three"}
print(Dict)
print(Dict.get(2))
print(Dict.get(4))
# with for loop get
for key in Dict:
	print(Dict.get(key),end=" ")