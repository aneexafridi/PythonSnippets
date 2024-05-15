# passing Array to Function
from array import *

def Show_Array(Array_values):
	print(Array_values)
	print(type(Array_values))
	for u in Array_values:
		print(u,end=' ')
Array = array('i',[11,22,33,44,55])
Show_Array(Array) # call the Function