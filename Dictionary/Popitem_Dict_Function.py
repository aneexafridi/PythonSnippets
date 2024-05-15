# ------------popitem() Method
# this method is used to remove the item which was last inserted into
# the Dictionary.
# It returns the removed item in the form of tuple, pairs are returned in LIFO order.
# (LIFO) last in first out
# Syntax:---
# 		Dict_Name.popitem()

Dict = {1:"one",2:"two",3:"three"}
print(Dict)
Dict.popitem()
print("\nAfter popitem from the Dict")
print(Dict)