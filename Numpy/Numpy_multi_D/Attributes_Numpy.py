from numpy import *
Array_A = array([[1,2],[3,4]])
Array_B = array([1,2,3,4])
# ndim - This attribute represents the number of dimensions
# or axes of the array.
# The number of dimensions is also refered as Rand.
# Syntax:-  Array_Name.ndim
print("Dimension",Array_A.ndim)
print("Dimension",Array_B.ndim)
# shape-- The attribute represent the shape of an Arrany.
# the shape is a tuple listing the number of elements
# along ach dimension.
# Syntax:- Array_Name.shape
print("\nShape",Array_A.shape)
print("Shape",Array_B.shape)
# size-- This Attribute represents the total number of elements
# in the Array.
# Syntax:--- Array_Name.size
print("\nSize",Array_A.size)
print("Size",Array_B.size)
# dtype-- This attribute represents the data type of elements
# in The Array.
# Syntax:- Array_Name.dtype
print("\ndtype",Array_A.dtype)
print("dtype",Array_B.dtype)
# nbytes-- This attribute represents the total number of bytes
# occupied by an array.
# Total number of bytes  = size of Array*item size of each element
# in Array
# Syntax:- Array_Name.nbytes
print("\nbytes",Array_A.nbytes)
print("bytes",Array_B.nbytes)