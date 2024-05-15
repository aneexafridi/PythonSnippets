from pandas import Series
from numpy import nan
# help(Series.map) # for more information

S = Series(data=['Ali',nan,'Fawad'],index=(1,2,3))
print(S)
print()
print('After the Series map method')

print(S.map(str.upper,na_action='ignore'))
# the map method app collection or dict or series
# if not founding on each value of series then
# converting that value into nan

