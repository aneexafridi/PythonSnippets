# view() Function
# This function is used to construct a new
# view of array wiht same data
# of existing array. The existing array and
# new array will share different memory locations
# If the new array get modified,the existing will
# be modified as the elements in both the array
# will be like mirror image.

# Ex:--       A = array([1,2,3,4])
# 			B = A.view()
from numpy import*
Array_A = array([1,2,3,4])
Array_B = Array_A.view()
Array_A[3] = 44
Array_B[0] = 99
print(Array_A)
print(Array_B)
print("Array_A",id(Array_A))
print("Array_B",id(Array_B))