from array import *
Array = array('i',[]) # created Empty Array
Size = int(input("Enter the Array Size: "))
for u in range(Size):
	Array.append(int(input("Enter: ")))
print(Array)
