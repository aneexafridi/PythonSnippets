# # array() Function of numpy is used to create
# # a multi dimensional array.
# # Syntax:- 
# # array(object,dtype=None,copy=True,order='K',subok=False,ndmin=0)
from numpy import *
Array = array([[1,2,3],[4,5,6]])
print(Array)
print("Accessing by Loops")
for m in range(len(Array)):
	for n in range(len(Array[m])):
		print(Array[m][n],end=' ')
	print()
# # for m in Array:  ## without index accessing
# # 	for n in m:
# # 		print(n,end=' ')
# # 	print()