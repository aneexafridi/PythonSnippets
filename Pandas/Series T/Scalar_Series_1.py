from pandas import Series
from numpy import arange

print(Series(data=5))
print()

#------------------Note--------------
# If data is a scalar value, an index must be provided.
# the value wil be repeated to match the length of "index"

print(Series(data=5,index=arange(5)))

print()
print(Series(data=5,index=[1,2,3]))