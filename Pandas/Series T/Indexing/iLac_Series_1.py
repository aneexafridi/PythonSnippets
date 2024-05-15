from pandas import Series

# Cannot index by location index with a non-integer key
S = Series(data=(1,2,3,4),index=list('abcd'))

print(S)
print('Index of c: ',S.iloc[2])