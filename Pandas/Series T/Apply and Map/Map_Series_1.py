from pandas import Series
# help(Series.map) # for more information

S = Series(data=['Ali','Equal','Fawad'],index=(1,2,3))
print(S)
print()
print('After the Series map method')

print(S.map({'Equal':'Shahab'}))
# the map method app collection or dict or series
# if not founding on each value of series then
# converting that value into nan

