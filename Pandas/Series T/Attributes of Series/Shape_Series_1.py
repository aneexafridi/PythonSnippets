from pandas import Series
S1 = Series(data=list('ABC'))
print(S1)
print('\nShape of Series: ',S1.shape)

print('\n')
List = [[1,2],['a','b']]
S2 = Series(data=List)
print(S2)
print('\nShape of Series: ',S2.shape)

