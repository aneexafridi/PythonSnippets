# the function is used to create an array with
# evently spaced numbers between a start point
# and stop point

# Syntax:-  Name_Array = linspace(start,stop,num=50,endpoint=True)
# num = is represent the numbers of part elements should be Divided
# Default is 50 and must be nonnegative number
from numpy import linspace
Linspace = linspace(1,10,num=5) # same (1,10,5)
print(Linspace)