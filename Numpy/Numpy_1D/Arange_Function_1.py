# Arrange() Function
# arange() function is used to create an array with a group of element
# from start to one element
# prior to stop in steps of stepsize.

# Syntax:-- Name_Arrange = arange(start,stop,stepsize,dtpye=None)
# stepsize -- Spacing between values. The default step size is 1.
from numpy import arange
Arange = arange(5)
print(Arange)
Arange = arange(-5,0)
print(Arange)
print('\n')
# same the range function can provide
print(list(range(-5,0)))