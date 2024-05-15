from pandas import Series

# take iAt based indexing can only have integer indexers

S = Series(data=('a','b','c'),index=['a','b','c'])
print(S)
print('At index: ',S.iat[0])