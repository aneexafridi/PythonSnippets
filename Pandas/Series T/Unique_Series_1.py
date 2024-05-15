from pandas import Series


# help(Series.unique)

S = Series(data=[1,2,3,2,3,1])
print(S)

print('\n')

print('After unique values of Series')
print(S.unique())