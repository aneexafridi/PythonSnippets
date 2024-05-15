# this function is used to create an array with evenly
# spaced numbers logarithmically. the sequence starts
# at the base **start(base to the power of start) and
# ends with base ** stop

# Syntax:- Name_Array = linspace(start,stop,num=50,endpoint=True
# base=10.0,dtype=None,axis=0)

# num = is represent the numbers of part elements should be Divided
# Default is 50 and must be nonnegative number

from numpy import *
Logspace = logspace(1,4,num=4,base=5)#default base=10
print(Logspace)