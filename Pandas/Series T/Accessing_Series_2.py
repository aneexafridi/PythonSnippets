# Data in the series can be accessed similar to that in an ndarray

from pandas import Series

S1 = Series(data=[1,2,3,4,5],index=['a','b','c','d','e'])
print(S1[0])
print('\n')
print(S1[:3])
print()
print(S1[-3:])

print()
for u in S1:
	print(u,end=' ')

