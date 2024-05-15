from pandas import Series
# help(Series.values)

S = Series(data=list('ABCE'))
print(S)
print('\nValues Attribute of Series')
print(S.values)
print('\n')

print(Series(data=('a','b','c')).values)