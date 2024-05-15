# -----------Empty Function
# empty() This function eturn a new array of given shape
# and type,without initializing entries.
# Syntax:---
# 		empty(shape, dtype=float, order='C')
		#hape : int or tuple of int e.g 2 or (2,3)
from numpy import *
Row = int(input("Enter the Row of Empty Array: "))
Column  = int(input("Enter the Column of Empty Array: "))
# U15 take 15 characters
Array = empty((Row,Column),dtype='U15') 
for u in range(Row):
	for v in range(Column):
		Array[u][v] = input("Enter String: ")
print(Array)
print("Length: ",len(Array))