# ----------Full Function
# This Function Return a new array of given shape and type,
# filled with fill_value.
# Syntax:--
# 		numpy.full(shape,fill_value,dtype=None,order='C')
# 		shape : int or sequence of ints
from numpy import *
# U5 mean  five character take the fil_value 
# and in this case shape 1D and with one Row,two colomn
Full = full(2,"Equal",dtype='U6') 
print(Full)
print()
# and in this case shape 1D and with Two Row,Three colomn
Full = full((2,3),"Equal",dtype="U5")
print(Full)