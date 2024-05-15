from pandas import Series
# help(Series.to_dict)
# Series index will be  key of Dict
# and value of Series will be the value of dict
S = Series(['a','b','c'])
print(S)
print('\nSeries To Dict')
print(S.to_dict())
print('\n')

S = Series(data={'a':11,'b':22,'c':33})
print('\nSeries to Dict')
print(S.to_dict())