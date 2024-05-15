from pandas import Series
from re import findall
# help(Series.replace) # for more information

S = Series(data=('a','S','9'))
print(S)
print()
print(S.replace(to_replace='S',value='E'))
print('\n')
print(S.replace(to_replace=findall('\\d','9'),value='Ze'))