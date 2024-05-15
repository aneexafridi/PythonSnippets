# -----------Empty Function
# empty() This function eturn a new array of given shape
# and type,without initializing entries.
# Syntax:---
# 		empty(shape, dtype=float, order='C')
		#hape : int or tuple of int e.g 2 or (2,3)
from numpy import *
Length = int(input("Enter the length of Empty Array: "))
# U15 take 15 characters
Array = empty(Length,dtype='U15') 
for u in range(Length):
	Array[u] = input("Enter String: ")
print(Array)
print("Length: ",len(Array))