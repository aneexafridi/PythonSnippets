from pandas import Series

# take only single argument

S = Series(data=('a','b','c'))
print(S)
print('At index: ',S.at[0])

S = Series(data=(1,2,3),index=list('abc'))
print(S)
print('At index: ',S.at['b'])