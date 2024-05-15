from pandas import Series
S = Series(data=list('ABC'))
print(S)
print('Attribute of Series ndim: ',S.ndim)

print('\n')

List = [(1,2),('a','b')]
S = Series(data=List)
print(S)
print('Attribute of Series ndim: ',S.ndim)