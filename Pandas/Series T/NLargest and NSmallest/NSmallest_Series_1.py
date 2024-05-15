from pandas import Series
# help(Series.nsmallest) # for more information

S = Series(data=(3,2,6,1,8,7),index=list('abcdef'))
print(S)

print('\n')
print('After the nlargest method use')
print(S.nsmallest(n=2))

