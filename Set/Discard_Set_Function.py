#-------------- Discard Method
# Discard() This does not raise an error if element does not exist in the Set.
# Syntax:--- Set_Name.discard(element)

Set = {1,2,'A',4}
print(Set)
print("After discard Method")
Set.discard(2)
print(Set)
print("if not found element then")
Set.discard(99)
print(Set)