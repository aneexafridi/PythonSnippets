from pandas import Series
# help(Series.apply) # for more information

S = Series(data=['Ali','Bilal','Equal'])
print(S)
print()
print('After the Series apply method for upper case')
print(S.apply(str.upper))