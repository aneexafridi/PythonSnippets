# -------Inserting/Adding new item
# We can add an item to dictionary just by mentioning a new key-value pair into
# an existing dictionary.
# If we mention a key which is already exists in the dictionary then the value
# gets update/modified rather then addding a new item.
# The new item my be added at any place in the dictionary as dictionary is an
# unordered collection.

Dict = {1:"one",2:"two",3:"three"}
print(Dict)
print(id(Dict))
print(type(Dict))
Dict[4] = "Four"
print("\nAfter Adding/inserting key-value")
print(Dict)
print(id(Dict))
print(type(Dict))
