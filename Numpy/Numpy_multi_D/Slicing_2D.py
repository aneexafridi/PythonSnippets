# for slicing 2D array
# Array[start:stop:step,start,stop,step]
from numpy import*
Array = array([[1,2,3],
			   [4,5,6],
			   [7,8,9]])
print(Array)
print("After Slicing the Array")
# print(Array[1:,1:])
# print(Array[1:,0:2])
# print(Array[0:2,1:])
# print(Array[0:2,0:2])
print(Array[0:2,0:])
# print(Array[:,1:2])
# print(Array[0:2,1:2])