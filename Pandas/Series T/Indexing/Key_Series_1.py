from pandas import Series

S = Series(data=(1,2,3),index=list('abc'))
print(S)
print()
print(S.keys()) # Returns Index of the Series