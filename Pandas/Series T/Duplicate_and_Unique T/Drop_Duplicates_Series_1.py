from pandas import Series
# help(Series.drop_duplicates)

S = Series(data=('cat','dog','cow','cat','dog'))
print(S)

print('\nDrop duplicates method use')
print(S.drop_duplicates())

# This method return the new Series
# without the duplicate data