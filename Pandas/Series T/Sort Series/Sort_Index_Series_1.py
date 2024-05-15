from pandas import Series
# help(Series.sort_index)

# Series.sort_index(axis=0, level=None, ascending=True, inplace=False,
# kind='quicksort', na_position='last', sort_remaining=True,
# ignore_index=False, key=None)[source]

print(list('adbc'))
S = Series(data=list('ADBC'),index=(4,1,3,2))

print(S)

print(S.sort_index(kind='quicksort'))
print(S.sort_index(ascending=False)) # default 