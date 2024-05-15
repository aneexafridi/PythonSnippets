# -----------pop() Methdo
# This method is used to remove the item with specified key.
# it returns the removed item's value.
# if key is not found then the default value is returned
# if key is not found an default value is not given then
# shows keyError.

# Synatx:---
# 			Dict_Name.pop(key,default_value)

Dict = {1:"one",2:"two",3:"three"}
print(Dict)
Dict.pop(2) # always give deflaut value
print("\nAfter the Pop from Dict")
print(Dict)
