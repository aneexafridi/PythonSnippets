from pandas import Series
S = Series(data=(1,2,3,4),index=list('abcd'))
print(S)

print('Index of c: ',S.loc['a'])

S = Series(data=(1,2,3,4))
print(S)
print(S.loc[3])