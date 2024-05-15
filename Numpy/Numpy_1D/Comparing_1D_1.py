# Comparing Arrays using numpy
# comparison operators can be used to compare arrays. the 
# size of array must be same.Comparing operators compares
# th corresponding element of the arrays and returns another
# arrays with Boolean value.
from numpy import *
Array_A = array([1,6,3,4])
Array_B = array([5,6,7,8])
Array_C= (Array_A==Array_B)
print(Array_A==Array_B)
# also !=,>=,<=,>,< check