# Reshape() Function
# Reshape functon convent 1D array into 2D array
# or 2D array into 1D array and so on etc

# Ex:- Array = array([1,2,3,4])
# 	A = reshape(Array(2,2))
from numpy import *
Array = array([1,2,3,4])
print(Array)
print("After Reshape")
print(reshape(Array,(2,2)))