# -----------Empty Function
# empty() This function eturn a new array of given shape
# and type,without initializing entries.
# Syntax:---
# 		empty(shape, dtype=float, order='C')
		#hape : int or tuple of int e.g 2 or (2,3)
from numpy import *
Array = empty(2,dtype=int)
print("The output Values are unassingned")
print(Array)
print("Length: ",len(Array))