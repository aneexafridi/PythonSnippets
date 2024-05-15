# ---------------------fromlist() method
# Append items from the list into Array.
# This is equivalent to for x in list: a.append(x)
# Note
# except that if there is a type error,
# the array is unchanged.
# Syntax: 
#  		array_Name.fromlist(list_Name)
from array import*
Array = array('i',[1,2,3])
print(Array)
print(type(Array))
List = [4,5,6]
print(List)
print(type(List))
print("\nAfter the use the fromlist method")
Array.fromlist(List)
print(Array)