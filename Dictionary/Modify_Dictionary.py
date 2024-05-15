# --------------Modify Diction
# We can modify the existing value of key by assigning 
# a new value.
# Dictionary doesn't create new object while when we modify values


Dict = {1:"one",2:"two",3:"three"}
print(Dict)
print(id(Dict))
print(type(Dict))
print("\nAfter modification in Dictionary")
Dict[3] = "THREE"
print(Dict)
print(id(Dict))
print(type(Dict))