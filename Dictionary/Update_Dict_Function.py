# -----------update() Method
# This method is used to update the dictionary
# with the specified key value pair.
# if key is already in the Dictionary then
# that key will be override 
# Syntax:--
# 		Dict_Name.update(iterable_object)

Dict = {1:"one",2:"two",3:"three"}
print(Dict)
Dict.update({4:"four"})
print("After updating the Dic")
print(Dict)

Dict_2 = {5:"five",6:"six",7:"seven"}
Dict.update(Dict_2)
print("After multi updating")
print(Dict)