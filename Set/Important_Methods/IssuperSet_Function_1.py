# -------- Issuperset() Function
# Issuperset() Test whether every element
# in other is in the set.
# Syntax:= 
# 		set >= other

Set_1 = {"A","B","F","G","Z"}
Set_2 = {"B","D","H","Z","A"}
print(Set_1)
print(Set_2)
print("After Set_1 Issuperset Set_2")
print(Set_1.issuperset(Set_2))

Set_3 = {"A","B","F","G","Z"}
Set_4 = {"Z","A"}
print(Set_3)
print(Set_4)
print("After Set_3 Issuperset Set_4")
print(Set_3.issuperset(Set_4))