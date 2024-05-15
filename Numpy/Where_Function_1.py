# where() Function
# this function is used to create a new Array which
# contains, returned element chosen from expression_1 or
# expression_2 "Depending" on condition.If condition is
# True expression_1 is executed else expression_2.

# Syntax:- numpy.where(condition,expression_1,expression_2)
# built-in function of Numpy
from numpy import *
A = array([1,2,13,4])
B = array([0,6,7,8])
C = where(A>B,A,B)
print(C)