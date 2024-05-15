from numpy import *
Array = array([[1,2],[3,4],[5,6]])
print(Array)
print()
print("axis=0",sum(Array,axis=0)) # Add Column
print("axis=1",sum(Array,axis=1)) # Add Row
print("Whole Sum of Array: ",sum(Array))

Ones =ones(4,dtype=int)
print(Ones)
print(sum(Ones))