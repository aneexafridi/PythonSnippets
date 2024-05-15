from numpy import *
#  Only pass numpy array to function
# def Numpy_Array(Array_data):
# 	print(type(Array_data))
# 	print(Array_data)

# Array = array([1,2,8,9])
# Numpy_Array(Array)

#  passing and return numpy array to function

def Numpy_Array(Array_data):
	print(type(Array_data))
	return Array_data

Array = array([1,2,8,9])
print(Numpy_Array(Array))