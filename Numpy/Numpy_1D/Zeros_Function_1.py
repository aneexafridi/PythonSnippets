# Zeros() Function
# This Function is used to create an array with all Zeros
# Syntax:- Zeros=zeros(shape,dtype=float,order='C')
# order  whether to store multi-dimensional data in row-major
# (C-style) or column-major
# (Fortran-style) order in memory. it can be C or F
from numpy import *
Zeros = zeros(5,dtype=int)# dtype set default float
print(Zeros)