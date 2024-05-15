# nonzero() Fucntion
# this function is used to determine the
# positions of elements which are non zero.
# this function returns an array that contains
# the indexes of the element of the array which
# are not equal to zero

# Syntax:-  result = nonzero(a)
from numpy import *
A = array([1,0,2,0,4])
result = nonzero(A)
print(result)