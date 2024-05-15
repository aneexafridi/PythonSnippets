#--------------------append() Method
#	The Append a new item with value x to
# 	the end of the array.
from array import*
Array = array('i',[]) # created Empty Array
print(Array)
print(len(Array))
print()
Array.append(11)
Array.append(99)
print(Array)
print(len(Array))