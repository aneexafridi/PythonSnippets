# Ones() Function
# This Function is used to create an array with all Zeros
# Syntax:- Ones = ones(shape,dtype=float,order='C')
# order  whether to store multi-dimensional data in row-major
# (C-style) or column-major
# (Fortran-style) order in memory. it can be C or F
from numpy import *
Ones = ones(5,dtype=int)# dtype set default float
print(Ones)