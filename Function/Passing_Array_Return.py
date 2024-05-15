# passing Array to Function
from array import *

def Show_Array(Array_values):
	print(type(Array_values))
	return Array_values
Array = array('i',[11,22,33,44,55])
print(Show_Array(Array)) # call the Function