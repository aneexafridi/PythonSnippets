from pandas import Series
from numpy import nan
# nan  is Not a Number
S = Series(data=['a','b','c'])
print(S)

print("Count S1 method")
print(S.count())

print()
S2 = Series(data=[1,2,3,nan])
print(S2)
# not count the NaN
print("Count S2 method")
print(S2.count())