# --------------issubset Function
# issubset() Test whether every element
# in other is in the set.

# Syntax:-- Set_1.intersection(Set_2)
			

Set_1 = {"A","B","F","G","Z"}
Set_2 = {"B","D","H","Z","A"}
print(Set_1)
print(Set_2)
print("After Set_1 InterSection Set_2")
print(Set_1.issubset(Set_2))
Set_3 = {"A","B","F","G","Z"}
Set_4 = {"B","Z","A"}
print(Set_3)
print(Set_4)
print("After Set_4 InterSection Set_3")
print(Set_4.issubset(Set_3))
