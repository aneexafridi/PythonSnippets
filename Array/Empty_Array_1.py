# Empty One-D Array
from array import*
Array = array('i',[]) # Empty Array created
print("Enter number: ")
for u in range(4):
	Array.append(int(input("Enter: "))) # add element at the end of Array
print("All Elements")
for u in range(4):
	print(Array[u],end=",")