# copy() Function
# this method is used to create a copy
# of an existing array. If the new array
# get modified, the existing array will
# not be affected or versa. Both
# the arrays are independent.
from numpy import *
Arrary_A = array([1,2,3,4])
Arrary_B = copy(Arrary_A)
print(Arrary_A)
print(Arrary_B)
print('\n')
Arrary_A[0] = 99
Arrary_B[3] = 77
print(Arrary_A)
print(Arrary_B)
print("Arrary_A",id(Arrary_A))
print("Arrary_B",id(Arrary_B))