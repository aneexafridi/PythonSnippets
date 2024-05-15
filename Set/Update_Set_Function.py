# ---------Adding multiple Elements
# we can add multiple elements to set using update() method.
# the update() method can take tuples,list,string,or others Sets
# as its argument.
# Syntax:-- Set_Name.update(elments)

Set = {1,2,3,4}
print(Set)
print("After update Set with Tuple")
Set.update(("Equal",99,22))# Tuple
print(Set)
print("\nAfter update Set with List")
Set.update([55,"Test"])
print(Set)
print("\nAfter update Set_A with String")
Set_A = {11,22}
Set_A.update("Hope")
print(Set_A)
